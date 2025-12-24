"""
RPC client for communicating with Kaspa nodes.

This module provides WebSocket-based RPC communication with Kaspa nodes,
supporting both JSON and Borsh encoding for efficient data transfer.

Example:
    >>> from kaspa_sdk.rpc import RpcClient, Encoding
    >>> from kaspa_sdk.core import NetworkId
    >>> 
    >>> async with RpcClient(
    ...     url="127.0.0.1",
    ...     network_id=NetworkId.TESTNET_10,
    ...     encoding=Encoding.BORSH
    ... ) as client:
    ...     info = await client.get_info()
    ...     print(info)
"""

from typing import Optional

__all__ = [
    # To be implemented
    # "RpcClient",
    # "Encoding",
]
