# Kaspa Python SDK Examples

This directory contains example scripts demonstrating how to use the Kaspa Python SDK.

## Prerequisites

```bash
# Install the SDK
pip install -e ..

# Or install from PyPI (when published)
pip install kaspa-sdk
```

## Running Examples

All examples are standalone Python scripts that can be run directly:

```bash
python examples/general/version.py
```

## Example Categories

### General Examples

Basic SDK usage and utility functions:

- **version.py** - Get SDK version information
- **rpc_connection.py** - Connect to a Kaspa node and retrieve information
- **unit_conversion.py** - Convert between KAS and Sompi units
- **address_validation.py** - Validate Kaspa addresses

### Wallet Examples (Coming Soon)

Wallet management and operations:

- **create_wallet.py** - Create a new HD wallet
- **restore_wallet.py** - Restore wallet from mnemonic
- **derive_addresses.py** - Derive addresses from HD wallet
- **balance_check.py** - Check wallet balance

### Transaction Examples (Coming Soon)

Transaction creation and management:

- **simple_transaction.py** - Create and send a basic transaction
- **batch_transactions.py** - Send multiple transactions
- **utxo_management.py** - Manage UTXOs

## Configuration

Some examples require a running Kaspa node. The default connection settings are:

- **Mainnet**: `ws://127.0.0.1:17110`
- **Testnet-11**: `ws://127.0.0.1:17310`

You can modify these in the example scripts or pass them as arguments.

## Notes

- Make sure you have a synced Kaspa node running if you want to test RPC examples
- For testnet examples, use testnet-11 addresses and configuration
- Private keys and mnemonics in examples are for demonstration only - never use them with real funds
