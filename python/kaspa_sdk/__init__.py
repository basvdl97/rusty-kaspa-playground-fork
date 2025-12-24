"""
Kaspa Python SDK

A comprehensive Python SDK for interacting with the Kaspa blockchain network.

This SDK provides:
- RPC client for node communication
- Wallet functionality (keys, addresses, transactions)
- Core blockchain primitives
- Utilities for common operations

Example:
    >>> from kaspa_sdk import RpcClient, NetworkId
    >>> async with RpcClient(url="127.0.0.1", network_id=NetworkId.TESTNET_10) as client:
    ...     info = await client.get_info()
    ...     print(f"Connected to {info.server_version}")
"""

from kaspa_sdk.version import __version__

# Core exports will be added as modules are implemented
__all__ = [
    "__version__",
    # RPC module exports (to be implemented)
    # "RpcClient",
    # "Encoding",
    # Wallet module exports (to be implemented)
    # "PrivateKey",
    # "PublicKey",
    # "Address",
    # Core module exports (to be implemented)
    # "NetworkId",
    # "NetworkType",
    # "Transaction",
    # Utility exports (to be implemented)
    # "kaspa_to_sompi",
    # "sompi_to_kaspa",
]
