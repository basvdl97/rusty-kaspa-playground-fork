# Kaspa Python SDK

[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

Python SDK for interacting with the Kaspa network. This SDK provides a Pythonic interface to the Kaspa blockchain, including RPC communication, wallet management, transaction creation, and cryptographic operations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Architecture](#architecture)
- [Examples](#examples)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Kaspa Python SDK is designed to provide a comprehensive, easy-to-use interface for Python developers to interact with the Kaspa blockchain network. It mirrors the functionality of the established [Kaspa WASM/JS SDK](../wasm/README.md) while following Python conventions and best practices.

## Features

### Current (Planned)

- **RPC Client** - WebSocket-based RPC client for communicating with Kaspa nodes
  - Async/await support using `asyncio`
  - Multiple encoding options (Borsh, JSON)
  - Automatic connection management and reconnection
  - Event-driven architecture with callbacks
  
- **Wallet Management** - Comprehensive wallet functionality
  - HD wallet support (BIP32/BIP44 derivation)
  - Mnemonic phrase generation and recovery (BIP39)
  - Address generation (standard and ECDSA)
  - Multiple account management
  
- **Transaction Handling** - Create, sign, and broadcast transactions
  - UTXO selection and management
  - Transaction building and signing
  - Fee calculation
  - Batch transaction support
  
- **Cryptographic Operations**
  - Key generation and derivation
  - Message signing and verification
  - Encryption/decryption using public/private keys
  - Address validation

- **Network Support**
  - Mainnet
  - Testnet-10
  - Testnet-11
  - Custom network configurations

## Installation

### From PyPI (once published)

```bash
pip install kaspa-sdk
```

### From Source

```bash
git clone https://github.com/kaspanet/rusty-kaspa.git
cd rusty-kaspa/python
pip install -e .
```

### Requirements

- Python 3.8 or higher
- Dependencies (automatically installed):
  - `websockets` - For WebSocket communication
  - `cryptography` - For cryptographic operations
  - `mnemonic` - For BIP39 mnemonic generation
  - `base58` - For address encoding
  - `pycryptodome` - For additional crypto operations

## Quick Start

### Connecting to a Kaspa Node

```python
import asyncio
from kaspa_sdk import RpcClient

async def main():
    # Create RPC client
    client = RpcClient(
        url="ws://127.0.0.1:17110",
        network_id="mainnet"
    )
    
    # Connect to the node
    await client.connect()
    
    # Get block DAG info
    info = await client.get_block_dag_info()
    print(f"Block count: {info['block_count']}")
    print(f"DAA Score: {info['virtual_daa_score']}")
    
    # Disconnect
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
```

### Creating a Wallet

```python
from kaspa_sdk import Wallet, Mnemonic

# Generate a new mnemonic
mnemonic = Mnemonic.generate()
print(f"Mnemonic: {mnemonic}")

# Create wallet from mnemonic
wallet = Wallet.from_mnemonic(
    mnemonic=mnemonic,
    network_id="testnet-11"
)

# Get receiving address
address = wallet.get_receive_address(account_index=0)
print(f"Address: {address}")
```

### Creating and Sending Transactions

```python
import asyncio
from kaspa_sdk import RpcClient, Wallet, kaspa_to_sompi

async def send_transaction():
    # Initialize client and wallet
    client = RpcClient(url="ws://127.0.0.1:17110", network_id="testnet-11")
    await client.connect()
    
    # Load wallet (use your own mnemonic)
    wallet = Wallet.from_mnemonic(
        mnemonic="your twelve word mnemonic phrase here ...",
        network_id="testnet-11"
    )
    
    # Get source address
    source_address = wallet.get_receive_address(account_index=0)
    
    # Define transaction parameters
    destination = "kaspatest:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl"
    amount_sompi = kaspa_to_sompi("0.5")  # 0.5 KAS
    
    # Get UTXOs
    utxos = await client.get_utxos_by_addresses([source_address])
    
    # Create transaction
    transaction = wallet.create_transaction(
        outputs=[{"address": destination, "amount": amount_sompi}],
        utxos=utxos["entries"],
        change_address=source_address,
        priority_fee=0
    )
    
    # Sign transaction
    signed_tx = wallet.sign_transaction(transaction)
    
    # Submit to network
    tx_id = await client.submit_transaction(signed_tx)
    print(f"Transaction submitted: {tx_id}")
    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(send_transaction())
```

## Documentation

Detailed documentation is available in the [`docs/`](docs/) directory:

- [API Reference](docs/api_reference.md) - Complete API documentation
- [RPC Guide](docs/rpc_guide.md) - Working with the RPC client
- [Wallet Guide](docs/wallet_guide.md) - Wallet management and operations
- [Transaction Guide](docs/transaction_guide.md) - Creating and managing transactions
- [Examples](examples/) - Code examples for common use cases

## Architecture

The SDK is organized into the following modules:

```
kaspa_sdk/
├── __init__.py           # Main package exports
├── rpc/                  # RPC client and related functionality
│   ├── __init__.py
│   ├── client.py         # WebSocket RPC client
│   ├── encoding.py       # Message encoding (Borsh/JSON)
│   └── types.py          # RPC request/response types
├── wallet/               # Wallet management
│   ├── __init__.py
│   ├── wallet.py         # Main wallet class
│   ├── account.py        # Account management
│   ├── keys.py           # Key generation and derivation
│   └── mnemonic.py       # BIP39 mnemonic support
├── transaction/          # Transaction handling
│   ├── __init__.py
│   ├── transaction.py    # Transaction creation and signing
│   ├── utxo.py           # UTXO management
│   └── fees.py           # Fee calculation
├── crypto/               # Cryptographic operations
│   ├── __init__.py
│   ├── keys.py           # Private/public key operations
│   ├── signing.py        # Message signing
│   └── address.py        # Address generation and validation
└── utils/                # Utility functions
    ├── __init__.py
    ├── encoding.py       # Base58, hex encoding
    ├── constants.py      # Network constants
    └── helpers.py        # Helper functions
```

## Examples

The [`examples/`](examples/) directory contains sample code demonstrating various SDK features:

### General Examples
- [`version.py`](examples/general/version.py) - Get SDK version
- [`rpc_connection.py`](examples/general/rpc_connection.py) - Connect to a node
- [`address_generation.py`](examples/general/address_generation.py) - Generate addresses
- [`key_derivation.py`](examples/general/key_derivation.py) - HD key derivation

### Wallet Examples
- [`create_wallet.py`](examples/wallet/create_wallet.py) - Create a new wallet
- [`restore_wallet.py`](examples/wallet/restore_wallet.py) - Restore from mnemonic
- [`balance_check.py`](examples/wallet/balance_check.py) - Check wallet balance

### Transaction Examples
- [`simple_transaction.py`](examples/transactions/simple_transaction.py) - Send a transaction
- [`batch_transactions.py`](examples/transactions/batch_transactions.py) - Send multiple transactions
- [`utxo_management.py`](examples/transactions/utxo_management.py) - UTXO operations

## Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/kaspanet/rusty-kaspa.git
cd rusty-kaspa/python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=kaspa_sdk --cov-report=html

# Run specific test file
pytest tests/unit/test_wallet.py
```

### Code Style

This project follows PEP 8 style guidelines with a maximum line length of 100 characters.

```bash
# Format code
black kaspa_sdk tests examples

# Check code style
flake8 kaspa_sdk tests examples

# Type checking
mypy kaspa_sdk
```

### Building Documentation

```bash
cd docs
make html
```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](../CONTRIBUTING.md) before submitting pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the ISC License - see the [LICENSE](LICENSE) file for details.

## Related Projects

- [Rusty Kaspa](https://github.com/kaspanet/rusty-kaspa) - Rust implementation of Kaspa node
- [Kaspa WASM SDK](../wasm/README.md) - JavaScript/TypeScript SDK
- [Kaspa Go](https://github.com/kaspanet/kaspad) - Original Go implementation

## Support

- **Documentation**: [https://kaspa.aspectron.org/](https://kaspa.aspectron.org/)
- **Discord**: [Kaspa Discord](https://discord.gg/kaspa)
- **GitHub Issues**: [Report bugs or request features](https://github.com/kaspanet/rusty-kaspa/issues)

## Acknowledgments

This SDK is inspired by and follows the design patterns of the Kaspa WASM SDK. Special thanks to the Kaspa development community for their contributions to the ecosystem.
