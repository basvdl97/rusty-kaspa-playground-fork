# Kaspa Python SDK

[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Python SDK for Kaspa - A high-performance, scalable blockchain platform built with Rust.

## Overview

The Kaspa Python SDK provides a comprehensive interface for interacting with the Kaspa blockchain network. It offers Python bindings for key management, transaction creation, and RPC communication with Kaspa nodes.

This SDK is designed to mirror the functionality of the [Kaspa WASM SDK](https://github.com/kaspanet/rusty-kaspa/tree/master/wasm) while providing a Pythonic API that feels natural to Python developers.

## Features

### Current Status: Alpha

This is an initial structure for the Kaspa Python SDK. The following features are planned:

### Planned Core Features

- **RPC API** — WebSocket-based RPC client for communicating with Kaspa nodes
  - Connect to Kaspa nodes (mainnet, testnet, devnet)
  - Query blockchain state and network information
  - Submit transactions
  - Subscribe to real-time notifications (blocks, transactions, etc.)

- **Wallet SDK** — Comprehensive wallet functionality
  - HD wallet support (BIP32/BIP44 derivation)
  - Key generation and management
  - Address creation and validation
  - Transaction creation and signing
  - UTXO management
  - Balance tracking

- **Core Primitives** — Essential blockchain primitives
  - Private/Public key operations
  - Address encoding/decoding
  - Transaction building
  - Script operations
  - Hash functions
  - Network type handling

## Installation

### From PyPI (Future)

```bash
pip install kaspa-sdk
```

### From Source

```bash
git clone https://github.com/kaspanet/rusty-kaspa.git
cd rusty-kaspa/python
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/kaspanet/rusty-kaspa.git
cd rusty-kaspa/python
pip install -e ".[dev]"
```

## Quick Start

### Basic Usage Example

```python
from kaspa_sdk import RpcClient, NetworkId, Encoding

# Create an RPC client
async with RpcClient(
    url="127.0.0.1",
    network_id=NetworkId.TESTNET_10,
    encoding=Encoding.BORSH
) as client:
    # Get node information
    info = await client.get_info()
    print(f"Node version: {info.server_version}")
    
    # Get current network state
    server_info = await client.get_server_info()
    print(f"Network: {server_info.network_name}")
    print(f"Synced: {server_info.is_synced}")
```

### Address Generation

```python
from kaspa_sdk import PrivateKey, NetworkType

# Generate a new private key
private_key = PrivateKey.random()

# Derive public key and address
public_key = private_key.to_public_key()
address = public_key.to_address(NetworkType.MAINNET)

print(f"Address: {address}")
```

### Transaction Creation

```python
from kaspa_sdk import (
    create_transaction,
    TransactionOutput,
    kaspa_to_sompi
)

# Create a transaction
outputs = [
    TransactionOutput(
        address="kaspa:qr0lr4ml9fn3chekrqmjdkergxl93l4wrk3dankcgvjq776s9wn9jkdskewva",
        amount=kaspa_to_sompi("0.5")  # 0.5 KAS
    )
]

transaction = await create_transaction(
    utxos=utxo_entries,
    outputs=outputs,
    change_address=source_address,
    priority_fee=0
)

# Sign transaction
await transaction.sign([private_key])

# Submit to network
tx_id = await transaction.submit(rpc_client)
print(f"Transaction ID: {tx_id}")
```

## SDK Structure

The SDK is organized into the following modules:

```
kaspa_sdk/
├── __init__.py          # Main package exports
├── version.py           # Version information
├── rpc/                 # RPC client and message types
│   ├── __init__.py
│   ├── client.py        # WebSocket RPC client
│   ├── messages.py      # RPC message definitions
│   └── types.py         # RPC-specific types
├── wallet/              # Wallet functionality
│   ├── __init__.py
│   ├── account.py       # HD wallet account management
│   ├── keys.py          # Key generation and derivation
│   ├── transaction.py   # Transaction creation and signing
│   └── utxo.py          # UTXO management
├── core/                # Core primitives
│   ├── __init__.py
│   ├── address.py       # Address encoding/decoding
│   ├── keys.py          # Private/public key operations
│   ├── network.py       # Network type definitions
│   ├── script.py        # Script operations
│   └── transaction.py   # Transaction primitives
└── utils/               # Utility functions
    ├── __init__.py
    ├── encoding.py      # Encoding utilities (Borsh, JSON)
    ├── crypto.py        # Cryptographic utilities
    └── conversion.py    # Unit conversion (KAS <-> Sompi)
```

## Examples

The `examples/` directory contains comprehensive examples:

### Basic Examples
- `version.py` - Check SDK version
- `address_generation.py` - Generate addresses from keys
- `mnemonic.py` - Mnemonic phrase generation and recovery
- `encryption.py` - Encrypt/decrypt data

### RPC Examples
- `rpc_connection.py` - Connect to a Kaspa node
- `get_balances.py` - Query address balances
- `subscribe_notifications.py` - Subscribe to network events

### Transaction Examples
- `simple_transaction.py` - Create and send a basic transaction
- `batch_transactions.py` - Handle multiple transactions
- `utxo_management.py` - Advanced UTXO handling

### Wallet Examples
- `create_wallet.py` - Create a new HD wallet
- `restore_wallet.py` - Restore wallet from mnemonic
- `wallet_operations.py` - Common wallet operations

## Documentation

Detailed documentation is available in the `docs/` directory:

- [Getting Started Guide](docs/getting-started.md)
- [API Reference](docs/api-reference.md)
- [RPC Client Guide](docs/rpc-client.md)
- [Wallet Guide](docs/wallet-guide.md)
- [Transaction Guide](docs/transactions.md)
- [Network Types](docs/networks.md)

## Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/kaspanet/rusty-kaspa.git
cd rusty-kaspa/python

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=kaspa_sdk --cov-report=html

# Run specific test file
pytest tests/test_address.py
```

### Code Quality

```bash
# Format code
black kaspa_sdk tests examples

# Lint code
ruff check kaspa_sdk tests examples

# Type checking
mypy kaspa_sdk
```

### Building Documentation

```bash
cd docs
make html
```

## Architecture

This Python SDK is designed to eventually bind to the Rust implementation of Kaspa using:

- **PyO3** - Rust bindings for Python
- **maturin** - Build and publish Rust-based Python packages

The initial structure provides:
1. Pure Python interfaces and type definitions
2. Placeholder implementations that will be replaced with Rust bindings
3. Comprehensive documentation and examples
4. Testing infrastructure

## Comparison with WASM SDK

| Feature | WASM SDK | Python SDK |
|---------|----------|------------|
| Target | Browser/Node.js | Python applications |
| Language | Rust → WASM → JS/TS | Rust → PyO3 → Python |
| RPC | WebSocket (wRPC) | WebSocket (wRPC) |
| Key Management | ✓ | Planned |
| Wallet Framework | ✓ | Planned |
| Transaction Creation | ✓ | Planned |
| HD Derivation | ✓ | Planned |
| Network Support | All | Planned |

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use type hints for all function signatures
- Write docstrings in Google style format
- Maintain test coverage above 80%

## Roadmap

### Phase 1: Foundation (Current)
- [x] Project structure and build configuration
- [x] Documentation framework
- [x] Example structure
- [ ] Core type definitions
- [ ] Pure Python RPC client prototype

### Phase 2: Rust Integration
- [ ] PyO3 bindings for key operations
- [ ] Rust-backed address generation
- [ ] Rust-backed transaction signing
- [ ] Rust-backed hash functions

### Phase 3: Feature Complete
- [ ] Full RPC client implementation
- [ ] HD wallet support
- [ ] Transaction creation and signing
- [ ] UTXO management
- [ ] Comprehensive test suite

### Phase 4: Production Ready
- [ ] Performance optimization
- [ ] Security audit
- [ ] Complete documentation
- [ ] PyPI release

## Related Projects

- [Rusty Kaspa](https://github.com/kaspanet/rusty-kaspa) - Rust implementation of Kaspa
- [Kaspa WASM SDK](https://github.com/kaspanet/rusty-kaspa/tree/master/wasm) - JavaScript/TypeScript SDK
- [kaspad](https://github.com/kaspanet/kaspad) - Original Go implementation

## License

This project is licensed under the ISC License - see the [LICENSE](../LICENSE) file for details.

## Support

- **Documentation**: https://kaspa.aspectron.org/
- **Issues**: https://github.com/kaspanet/rusty-kaspa/issues
- **Discord**: https://discord.gg/kaspa
- **Website**: https://kaspa.org/

## Acknowledgments

This SDK is inspired by and designed to complement the [Kaspa WASM SDK](https://github.com/kaspanet/rusty-kaspa/tree/master/wasm). Many design decisions and API patterns are based on the proven WASM implementation.
