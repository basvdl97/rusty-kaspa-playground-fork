"""
Kaspa Python SDK

A comprehensive Python SDK for interacting with the Kaspa blockchain network.

This SDK provides:
- RPC client for node communication
- Wallet management and key derivation
- Transaction creation and signing
- Cryptographic operations
- Utility functions

Basic usage:

    from kaspa_sdk import RpcClient, Wallet
    
    # Connect to a node
    client = RpcClient(url="ws://127.0.0.1:17110", network_id="mainnet")
    await client.connect()
    
    # Create or load a wallet
    wallet = Wallet.from_mnemonic(mnemonic="...", network_id="mainnet")
    
    # Get an address
    address = wallet.get_receive_address(account_index=0)
"""

from kaspa_sdk.__version__ import __version__, __author__, __license__

# Core imports - will be implemented
# from kaspa_sdk.rpc import RpcClient, RpcEventType
# from kaspa_sdk.wallet import Wallet, Account
# from kaspa_sdk.crypto import PrivateKey, PublicKey, Address
# from kaspa_sdk.transaction import Transaction, TransactionOutput, TransactionInput
# from kaspa_sdk.utils import kaspa_to_sompi, sompi_to_kaspa, validate_address

__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__license__",
    
    # Core classes - to be uncommented as implemented
    # "RpcClient",
    # "RpcEventType",
    # "Wallet",
    # "Account",
    # "PrivateKey",
    # "PublicKey",
    # "Address",
    # "Transaction",
    # "TransactionOutput",
    # "TransactionInput",
    
    # Utility functions - to be uncommented as implemented
    # "kaspa_to_sompi",
    # "sompi_to_kaspa",
    # "validate_address",
]

# Package metadata
__title__ = "kaspa-sdk"
__description__ = "Python SDK for the Kaspa blockchain network"
__url__ = "https://github.com/kaspanet/rusty-kaspa"
__doc__ = __description__ + " <" + __url__ + ">"
