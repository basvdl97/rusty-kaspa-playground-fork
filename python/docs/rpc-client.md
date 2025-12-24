# RPC Client Guide

Guide to using the Kaspa RPC client for node communication.

## Overview

The RPC client provides WebSocket-based communication with Kaspa nodes. It supports both JSON and Borsh encoding for efficient data transfer.

## Connection

### Basic Connection

```python
from kaspa_sdk.rpc import RpcClient, Encoding
from kaspa_sdk.core import NetworkId

# Create and connect to a node
async with RpcClient(
    url="127.0.0.1",
    network_id=NetworkId.TESTNET_10,
    encoding=Encoding.BORSH
) as client:
    # Client is connected and ready
    info = await client.get_info()
```

### Manual Connection Management

```python
client = RpcClient(
    url="127.0.0.1",
    network_id=NetworkId.TESTNET_10
)

try:
    await client.connect()
    # Use client
finally:
    await client.disconnect()
```

## Encoding Options

### Borsh (Binary)

Borsh encoding is more efficient and recommended for production:

```python
client = RpcClient(
    url="127.0.0.1",
    network_id=NetworkId.TESTNET_10,
    encoding=Encoding.BORSH  # Default
)
```

### JSON (Text)

JSON encoding is human-readable and useful for debugging:

```python
client = RpcClient(
    url="127.0.0.1",
    network_id=NetworkId.TESTNET_10,
    encoding=Encoding.JSON
)
```

## RPC Methods

### Node Information

```python
# Get node information
info = await client.get_info()
print(f"Server version: {info.server_version}")

# Get server and network info
server_info = await client.get_server_info()
print(f"Is synced: {server_info.is_synced}")
print(f"Network: {server_info.network_name}")
```

### Block DAG Information

```python
# Get block DAG info
dag_info = await client.get_block_dag_info()
print(f"Block count: {dag_info.block_count}")
print(f"Difficulty: {dag_info.difficulty}")
```

### UTXO Queries

```python
# Get UTXOs for addresses
addresses = [
    "kaspatest:qq123...",
    "kaspatest:qq456...",
]

result = await client.get_utxos_by_addresses(addresses)
for entry in result.entries:
    print(f"UTXO: {entry.outpoint} - {entry.amount} sompi")
```

### Balance Queries

```python
# Get balance for an address
balance = await client.get_balance_by_address("kaspatest:qq123...")
print(f"Balance: {balance.balance} sompi")
```

### Transaction Submission

```python
# Submit a signed transaction
tx_id = await client.submit_transaction(transaction)
print(f"Transaction submitted: {tx_id}")
```

### Network State

```python
# Get current blue score
blue_score = await client.get_virtual_selected_parent_blue_score()
print(f"Current blue score: {blue_score}")
```

## Error Handling

```python
from kaspa_sdk.rpc import RpcClient
from kaspa_sdk.core import NetworkId

async def connect_with_retry():
    client = RpcClient(
        url="127.0.0.1",
        network_id=NetworkId.TESTNET_10
    )
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            await client.connect()
            print("Connected successfully")
            return client
        except ConnectionError as e:
            print(f"Connection attempt {attempt + 1} failed: {e}")
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2)
```

## Network Selection

### Mainnet

```python
client = RpcClient(
    url="mainnet-node.kaspa.org",
    network_id=NetworkId.MAINNET
)
```

### Testnet

```python
# Testnet 10
client = RpcClient(
    url="127.0.0.1",
    network_id=NetworkId.TESTNET_10
)

# Testnet 11
client = RpcClient(
    url="127.0.0.1",
    network_id=NetworkId.TESTNET_11
)
```

### Custom Port

```python
# Use a custom port instead of the default
client = RpcClient(
    url="127.0.0.1",
    network_id=NetworkId.TESTNET_10,
    port=12345
)
```

## Best Practices

1. **Use context managers** - Always use `async with` for automatic cleanup
2. **Check sync status** - Verify the node is synced before operations
3. **Handle errors** - Implement proper error handling and retries
4. **Use Borsh encoding** - More efficient than JSON for production
5. **Close connections** - Always disconnect when done

## Example: Full Workflow

```python
import asyncio
from kaspa_sdk.rpc import RpcClient, Encoding
from kaspa_sdk.core import NetworkId

async def main():
    # Connect to node
    async with RpcClient(
        url="127.0.0.1",
        network_id=NetworkId.TESTNET_10,
        encoding=Encoding.BORSH
    ) as client:
        # Check node status
        server_info = await client.get_server_info()
        
        if not server_info.is_synced:
            print("Node is not synced. Please wait.")
            return
        
        print(f"Connected to {server_info.network_name}")
        print(f"Node version: {server_info.server_version}")
        
        # Get network state
        dag_info = await client.get_block_dag_info()
        print(f"Block count: {dag_info.block_count}")
        
        # Query address balance
        address = "kaspatest:qq123..."
        balance = await client.get_balance_by_address(address)
        print(f"Balance: {balance.balance} sompi")

if __name__ == "__main__":
    asyncio.run(main())
```

## Future Features

The RPC client will support additional features:

- [ ] Real-time notifications (blocks, transactions)
- [ ] Subscription management
- [ ] Connection pooling
- [ ] Automatic reconnection
- [ ] Request batching
- [ ] Response caching
