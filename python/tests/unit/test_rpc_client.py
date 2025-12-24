"""
Unit tests for RPC client
"""

import pytest
from kaspa_sdk.rpc.client import RpcClient, Encoding


class TestRpcClient:
    """Test RPC client initialization and configuration."""
    
    def test_client_creation(self):
        """Test creating an RPC client with default parameters."""
        client = RpcClient()
        assert client.url == "ws://127.0.0.1:17110"
        assert client.network_id == "mainnet"
        assert client.encoding == Encoding.BORSH
        assert client.connected is False
    
    def test_client_custom_url(self):
        """Test creating an RPC client with custom URL."""
        client = RpcClient(url="ws://example.com:17110")
        assert client.url == "ws://example.com:17110"
    
    def test_client_network_id(self):
        """Test creating an RPC client with different network IDs."""
        client = RpcClient(network_id="testnet-11")
        assert client.network_id == "testnet-11"
    
    def test_client_encoding(self):
        """Test creating an RPC client with different encodings."""
        client = RpcClient(encoding=Encoding.JSON)
        assert client.encoding == Encoding.JSON
    
    def test_client_timeout(self):
        """Test creating an RPC client with custom timeout."""
        client = RpcClient(timeout=60)
        assert client.timeout == 60


class TestEventHandling:
    """Test event handling functionality."""
    
    def test_add_event_listener(self):
        """Test adding event listeners."""
        client = RpcClient()
        
        def handler(event):
            pass
        
        client.add_event_listener("connect", handler)
        assert "connect" in client._event_handlers
        assert handler in client._event_handlers["connect"]
    
    def test_add_multiple_event_listeners(self):
        """Test adding listeners for multiple events."""
        client = RpcClient()
        
        def handler(event):
            pass
        
        client.add_event_listener(["connect", "disconnect"], handler)
        assert handler in client._event_handlers["connect"]
        assert handler in client._event_handlers["disconnect"]
    
    def test_remove_event_listener(self):
        """Test removing event listeners."""
        client = RpcClient()
        
        def handler(event):
            pass
        
        client.add_event_listener("connect", handler)
        client.remove_event_listener("connect", handler)
        assert handler not in client._event_handlers.get("connect", [])


# Integration tests would go here but require a running node
@pytest.mark.skip(reason="Requires running Kaspa node")
class TestRpcIntegration:
    """Integration tests for RPC client (requires running node)."""
    
    @pytest.mark.asyncio
    async def test_connect_disconnect(self):
        """Test connecting and disconnecting from a node."""
        client = RpcClient(url="ws://127.0.0.1:17110")
        await client.connect()
        assert client.connected is True
        await client.disconnect()
        assert client.connected is False
    
    @pytest.mark.asyncio
    async def test_get_info(self):
        """Test getting node info."""
        client = RpcClient(url="ws://127.0.0.1:17110")
        await client.connect()
        info = await client.get_info()
        assert "serverVersion" in info
        await client.disconnect()
