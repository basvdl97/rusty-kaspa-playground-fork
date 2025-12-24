# Getting Started with Kaspa Python SDK

This guide will help you get started with the Kaspa Python SDK.

## Installation

### Requirements

- Python 3.8 or higher
- pip (Python package manager)

### Install from PyPI (Future)

Once published to PyPI, you'll be able to install the SDK with:

```bash
pip install kaspa-sdk
```

### Install from Source

To install the latest development version:

```bash
git clone https://github.com/kaspanet/rusty-kaspa.git
cd rusty-kaspa/python
pip install -e .
```

For development with all tools:

```bash
pip install -e ".[dev]"
```

## Quick Start

### Basic Usage

```python
from kaspa_sdk import __version__

print(f"Kaspa SDK version: {__version__}")
```

### Working with Networks

```python
from kaspa_sdk.core import NetworkId, NetworkType

# Create network identifier
network = NetworkId.TESTNET_10
print(f"Network: {network}")
print(f"Default port: {network.default_port}")
```

### Unit Conversion

```python
from kaspa_sdk.utils.conversion import kaspa_to_sompi, sompi_to_kaspa

# Convert KAS to sompi
sompi = kaspa_to_sompi("1.5")
print(f"1.5 KAS = {sompi} sompi")

# Convert sompi to KAS
kas = sompi_to_kaspa(150000000)
print(f"150,000,000 sompi = {kas} KAS")
```

## Running Examples

The SDK includes several example scripts in the `examples/` directory:

### Basic Examples

```bash
# Check SDK version
python examples/basic/version.py

# Unit conversion examples
python examples/basic/conversion.py

# Network types
python examples/basic/networks.py
```

### Future Examples (Not Yet Implemented)

These examples will be available once the core functionality is implemented:

```bash
# RPC examples
python examples/basic/rpc_connection.py

# Transaction examples
python examples/transactions/simple_transaction.py

# Wallet examples
python examples/wallet/create_wallet.py
```

## Next Steps

- Read the [API Reference](api-reference.md) for detailed documentation
- Check out the [RPC Client Guide](rpc-client.md) for node communication
- Learn about [Wallet Management](wallet-guide.md)
- Explore [Transaction Creation](transactions.md)

## Development Status

**Current Status: Alpha / Structure Phase**

The Python SDK is in early development. The current release includes:

✅ Project structure and build configuration
✅ Documentation framework
✅ Type definitions for core concepts
✅ Example structure
✅ Unit conversion utilities

🚧 In Development:
- RPC client implementation
- Wallet functionality
- Transaction building
- Rust bindings via PyO3

## Getting Help

- **Documentation**: https://kaspa.aspectron.org/
- **Issues**: https://github.com/kaspanet/rusty-kaspa/issues
- **Discord**: https://discord.gg/kaspa

## Contributing

We welcome contributions! See the main README for contribution guidelines.
