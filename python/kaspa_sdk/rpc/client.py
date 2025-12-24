"""
RPC Client Implementation

Provides WebSocket-based RPC client for communicating with Kaspa nodes.
"""

import asyncio
import json
from typing import Any, Callable, Dict, List, Optional, Union
from enum import Enum

try:
    import websockets
    from websockets.client import WebSocketClientProtocol
except ImportError:
    websockets = None  # type: ignore
    WebSocketClientProtocol = None  # type: ignore


class Encoding(Enum):
    """Message encoding types for RPC communication."""
    BORSH = "borsh"
    JSON = "json"


class RpcClient:
    """
    WebSocket-based RPC client for Kaspa nodes.
    
    Supports async/await operations and event-driven architecture.
    
    Example:
        >>> client = RpcClient(url="ws://127.0.0.1:17110", network_id="mainnet")
        >>> await client.connect()
        >>> info = await client.get_block_dag_info()
        >>> await client.disconnect()
    
    Args:
        url: WebSocket URL of the Kaspa node (e.g., "ws://127.0.0.1:17110")
        network_id: Network identifier ("mainnet", "testnet-10", "testnet-11")
        encoding: Message encoding type (Encoding.BORSH or Encoding.JSON)
        timeout: Connection timeout in seconds
        
    Attributes:
        url: The node URL
        network_id: The network identifier
        connected: Whether the client is currently connected
    """
    
    def __init__(
        self,
        url: str = "ws://127.0.0.1:17110",
        network_id: str = "mainnet",
        encoding: Encoding = Encoding.BORSH,
        timeout: int = 30,
    ):
        """Initialize the RPC client."""
        if websockets is None:
            raise ImportError(
                "websockets package is required for RPC client. "
                "Install it with: pip install websockets"
            )
        
        self.url = url
        self.network_id = network_id
        self.encoding = encoding
        self.timeout = timeout
        self._ws: Optional[WebSocketClientProtocol] = None
        self._connected = False
        self._event_handlers: Dict[str, List[Callable]] = {}
        self._request_id = 0
    
    @property
    def connected(self) -> bool:
        """Check if the client is connected."""
        return self._connected
    
    async def connect(self) -> None:
        """
        Connect to the Kaspa node.
        
        Raises:
            ConnectionError: If connection fails
        """
        try:
            self._ws = await websockets.connect(self.url, timeout=self.timeout)  # type: ignore
            self._connected = True
            await self._emit_event("connect", {})
        except Exception as e:
            raise ConnectionError(f"Failed to connect to {self.url}: {e}")
    
    async def disconnect(self) -> None:
        """
        Disconnect from the Kaspa node.
        """
        if self._ws:
            await self._ws.close()
            self._connected = False
            await self._emit_event("disconnect", {})
    
    def add_event_listener(
        self,
        event_type: Union[str, List[str]],
        callback: Callable,
    ) -> None:
        """
        Add an event listener.
        
        Args:
            event_type: Event type(s) to listen for
            callback: Callback function to invoke on event
        """
        if isinstance(event_type, str):
            event_type = [event_type]
        
        for evt in event_type:
            if evt not in self._event_handlers:
                self._event_handlers[evt] = []
            self._event_handlers[evt].append(callback)
    
    def remove_event_listener(
        self,
        event_type: str,
        callback: Callable,
    ) -> None:
        """
        Remove an event listener.
        
        Args:
            event_type: Event type
            callback: Callback function to remove
        """
        if event_type in self._event_handlers:
            try:
                self._event_handlers[event_type].remove(callback)
            except ValueError:
                pass
    
    async def _emit_event(self, event_type: str, data: Any) -> None:
        """Emit an event to all registered handlers."""
        if event_type in self._event_handlers:
            for handler in self._event_handlers[event_type]:
                if asyncio.iscoroutinefunction(handler):
                    await handler({"type": event_type, "data": data})
                else:
                    handler({"type": event_type, "data": data})
    
    async def _send_request(self, method: str, params: Optional[Dict] = None) -> Any:
        """
        Send an RPC request and wait for response.
        
        Args:
            method: RPC method name
            params: Method parameters
            
        Returns:
            Response data
            
        Raises:
            RuntimeError: If not connected
            Exception: On RPC error
        """
        if not self._connected or not self._ws:
            raise RuntimeError("Not connected to node")
        
        self._request_id += 1
        request = {
            "jsonrpc": "2.0",
            "id": self._request_id,
            "method": method,
            "params": params or {},
        }
        
        # Send request
        await self._ws.send(json.dumps(request))
        
        # Wait for response
        response_str = await self._ws.recv()
        response = json.loads(response_str)
        
        if "error" in response:
            raise Exception(f"RPC error: {response['error']}")
        
        return response.get("result")
    
    # Core RPC methods based on Kaspa WASM SDK
    
    async def get_block_dag_info(self) -> Dict[str, Any]:
        """
        Get block DAG information.
        
        Returns:
            Dictionary with DAG info including block_count, virtual_daa_score, etc.
        """
        return await self._send_request("getBlockDagInfo")
    
    async def get_info(self) -> Dict[str, Any]:
        """
        Get node information.
        
        Returns:
            Dictionary with node info
        """
        return await self._send_request("getInfo")
    
    async def get_server_info(self) -> Dict[str, Any]:
        """
        Get server information including sync status.
        
        Returns:
            Dictionary with server info and is_synced status
        """
        return await self._send_request("getServerInfo")
    
    async def get_utxos_by_addresses(
        self,
        addresses: List[str],
    ) -> Dict[str, Any]:
        """
        Get UTXOs for the given addresses.
        
        Args:
            addresses: List of Kaspa addresses
            
        Returns:
            Dictionary with entries list of UTXOs
        """
        return await self._send_request(
            "getUtxosByAddresses",
            {"addresses": addresses}
        )
    
    async def get_balance_by_address(self, address: str) -> Dict[str, Any]:
        """
        Get balance for a specific address.
        
        Args:
            address: Kaspa address
            
        Returns:
            Dictionary with balance information
        """
        return await self._send_request(
            "getBalanceByAddress",
            {"address": address}
        )
    
    async def get_balances_by_addresses(
        self,
        addresses: List[str],
    ) -> Dict[str, Any]:
        """
        Get balances for multiple addresses.
        
        Args:
            addresses: List of Kaspa addresses
            
        Returns:
            Dictionary with balance entries for each address
        """
        return await self._send_request(
            "getBalancesByAddresses",
            {"addresses": addresses}
        )
    
    async def submit_transaction(self, transaction: Dict[str, Any]) -> str:
        """
        Submit a signed transaction to the network.
        
        Args:
            transaction: Signed transaction object
            
        Returns:
            Transaction ID
        """
        result = await self._send_request(
            "submitTransaction",
            {"transaction": transaction}
        )
        return result.get("transactionId")
    
    async def get_block(self, block_hash: str, include_transactions: bool = False) -> Dict[str, Any]:
        """
        Get block by hash.
        
        Args:
            block_hash: Block hash
            include_transactions: Whether to include transactions
            
        Returns:
            Block data
        """
        return await self._send_request(
            "getBlock",
            {
                "hash": block_hash,
                "includeTransactions": include_transactions,
            }
        )
    
    async def get_virtual_chain_from_block(
        self,
        start_hash: str,
        include_accepted_transaction_ids: bool = False,
    ) -> Dict[str, Any]:
        """
        Get virtual chain from a starting block.
        
        Args:
            start_hash: Starting block hash
            include_accepted_transaction_ids: Include transaction IDs
            
        Returns:
            Virtual chain data
        """
        return await self._send_request(
            "getVirtualChainFromBlock",
            {
                "startHash": start_hash,
                "includeAcceptedTransactionIds": include_accepted_transaction_ids,
            }
        )
    
    # Subscription methods (to be implemented with proper event handling)
    
    async def subscribe_virtual_daa_score_changed(
        self,
        callback: Callable,
    ) -> None:
        """
        Subscribe to virtual DAA score changes.
        
        Args:
            callback: Callback function to invoke on changes
        """
        # TODO: Implement subscription logic
        self.add_event_listener("virtual_daa_score_changed", callback)
        await self._send_request("subscribeVirtualDaaScoreChanged")
    
    async def unsubscribe_virtual_daa_score_changed(self) -> None:
        """Unsubscribe from virtual DAA score changes."""
        await self._send_request("unsubscribeVirtualDaaScoreChanged")
