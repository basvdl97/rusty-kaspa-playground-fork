# Getting Started with Kaspa Python SDK

## Installation

### From PyPI (Recommended)

Once published, install via pip:

```bash
pip install kaspa-sdk
```

### From Source

For development or testing:

```bash
# Clone the repository
git clone https://github.com/kaspanet/rusty-kaspa.git
cd rusty-kaspa/python

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Quick Start

### 1. Connecting to a Node

```python
import asyncio
from kaspa_sdk.rpc.client import RpcClient

async def main():
    client = RpcClient(url="ws://127.0.0.1:17110", network_id="mainnet")
    await client.connect()
    
    info = await client.get_block_dag_info()
    print(f"Block count: {info['blockCount']}")
    
    await client.disconnect()

asyncio.run(main())
```

### 2. Working with Addresses

```python
from kaspa_sdk.utils.helpers import validate_address, get_network_prefix

# Validate an address
address = "kaspa:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl"
is_valid = validate_address(address, "mainnet")
print(f"Address valid: {is_valid}")

# Get network prefix
prefix = get_network_prefix("testnet-11")
print(f"Testnet prefix: {prefix}")
```

### 3. Unit Conversion

```python
from kaspa_sdk.utils.helpers import kaspa_to_sompi, sompi_to_kaspa

# Convert KAS to Sompi
sompi = kaspa_to_sompi("1.5")
print(f"1.5 KAS = {sompi} Sompi")

# Convert Sompi to KAS
kas = sompi_to_kaspa(150_000_000)
print(f"150000000 Sompi = {kas} KAS")
```

## Next Steps

- Check out the [examples](../examples/) directory for more code samples
- Read the [RPC Guide](rpc_guide.md) for detailed RPC usage
- See the [API Reference](api_reference.md) for complete documentation

## Requirements

- Python 3.8 or higher
- A running Kaspa node (for RPC operations)
- Internet connection (for connecting to remote nodes)

## Troubleshooting

### Connection Issues

If you can't connect to a node:

1. Make sure the node is running and synced
2. Check the RPC port is correct for your network
3. Verify firewall settings allow WebSocket connections

### Import Errors

If you get import errors:

```bash
# Reinstall the package
pip uninstall kaspa-sdk
pip install kaspa-sdk

# Or for development
pip install -e .
```

## Support

- GitHub Issues: [Report bugs](https://github.com/kaspanet/rusty-kaspa/issues)
- Discord: [Join the community](https://discord.gg/kaspa)
- Documentation: [Read the docs](https://kaspa.aspectron.org/)
