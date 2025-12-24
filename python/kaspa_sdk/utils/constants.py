"""
Utility Constants

Network configurations and constants for the Kaspa network.
"""

from typing import Dict, Any

# Sompi conversion constant (1 KAS = 10^8 Sompi)
SOMPI_PER_KASPA = 100_000_000

# Network configurations
NETWORKS: Dict[str, Dict[str, Any]] = {
    "mainnet": {
        "name": "mainnet",
        "prefix": "kaspa",
        "default_port": 16110,
        "rpc_port": 17110,
    },
    "testnet-10": {
        "name": "testnet-10",
        "prefix": "kaspatest",
        "default_port": 16210,
        "rpc_port": 17210,
    },
    "testnet-11": {
        "name": "testnet-11",
        "prefix": "kaspatest",
        "default_port": 16310,
        "rpc_port": 17310,
    },
    "simnet": {
        "name": "simnet",
        "prefix": "kaspasim",
        "default_port": 16510,
        "rpc_port": 17510,
    },
    "devnet": {
        "name": "devnet",
        "prefix": "kaspadev",
        "default_port": 16610,
        "rpc_port": 17610,
    },
}

# BIP32/BIP44 constants
BIP32_HARDENED_BIT = 0x80000000
BIP44_PURPOSE = 44
BIP44_COIN_TYPE = 111111  # Kaspa coin type

# Address version bytes
ADDRESS_VERSION = 0

# Transaction constants
DEFAULT_PRIORITY_FEE = 0
MINIMUM_RELAY_TRANSACTION_FEE = 1000
MAX_STANDARD_TRANSACTION_MASS = 100000

# Script constants
MAX_SCRIPT_PUBLIC_KEY_VERSION = 0
