# RPC Client Guide

The RPC client provides WebSocket-based communication with Kaspa nodes.

## Basic Usage

### Creating a Client

```python
from kaspa_sdk.rpc.client import RpcClient, Encoding

# Connect to local node
client = RpcClient(
    url="ws://127.0.0.1:17110",
    network_id="mainnet",
    encoding=Encoding.BORSH,  # or Encoding.JSON
    timeout=30
)
```

### Connection Management

```python
import asyncio

async def example():
    # Connect
    await client.connect()
    print(f"Connected: {client.connected}")
    
    # Perform operations...
    
    # Disconnect
    await client.disconnect()

asyncio.run(example())
```

### Using Context Manager (Future Feature)

```python
async def example():
    async with RpcClient(url="ws://127.0.0.1:17110") as client:
        info = await client.get_info()
        print(info)
```

## Core RPC Methods

### Node Information

```python
# Get general node info
info = await client.get_info()
print(f"Version: {info['serverVersion']}")

# Get server info with sync status
server_info = await client.get_server_info()
print(f"Synced: {server_info['isSynced']}")

# Get block DAG info
dag_info = await client.get_block_dag_info()
print(f"Blocks: {dag_info['blockCount']}")
```

### Balance and UTXO Queries

```python
# Get balance for an address
balance = await client.get_balance_by_address(
    "kaspa:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl"
)
print(f"Balance: {balance['balance']} Sompi")

# Get UTXOs for addresses
utxos = await client.get_utxos_by_addresses([
    "kaspa:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl"
])
print(f"UTXO count: {len(utxos['entries'])}")

# Get balances for multiple addresses
balances = await client.get_balances_by_addresses([
    "kaspa:address1...",
    "kaspa:address2..."
])
```

### Block Operations

```python
# Get block by hash
block = await client.get_block(
    block_hash="abc123...",
    include_transactions=True
)

# Get virtual chain from block
chain = await client.get_virtual_chain_from_block(
    start_hash="abc123...",
    include_accepted_transaction_ids=True
)
```

### Transaction Submission

```python
# Submit a signed transaction
tx_id = await client.submit_transaction(signed_transaction)
print(f"Transaction ID: {tx_id}")
```

## Event Handling

### Adding Event Listeners

```python
def on_connect(event):
    print(f"Connected! Event: {event}")

def on_disconnect(event):
    print(f"Disconnected! Event: {event}")

# Add listeners
client.add_event_listener("connect", on_connect)
client.add_event_listener("disconnect", on_disconnect)

# Multiple events with one listener
client.add_event_listener(["connect", "disconnect"], on_status_change)
```

### Async Event Handlers

```python
async def on_data(event):
    # Async processing
    await process_event(event['data'])

client.add_event_listener("data", on_data)
```

### Subscriptions

```python
async def on_daa_score_changed(event):
    print(f"New DAA Score: {event['data']}")

# Subscribe to DAA score changes
await client.subscribe_virtual_daa_score_changed(on_daa_score_changed)

# Unsubscribe
await client.unsubscribe_virtual_daa_score_changed()
```

## Error Handling

```python
from kaspa_sdk.rpc.client import RpcClient

async def safe_rpc_call():
    client = RpcClient(url="ws://127.0.0.1:17110")
    
    try:
        await client.connect()
        info = await client.get_info()
        return info
    except ConnectionError as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"RPC error: {e}")
    finally:
        if client.connected:
            await client.disconnect()
```

## Network Configuration

### Mainnet

```python
client = RpcClient(
    url="ws://127.0.0.1:17110",
    network_id="mainnet"
)
```

### Testnet-11

```python
client = RpcClient(
    url="ws://127.0.0.1:17310",
    network_id="testnet-11"
)
```

### Remote Nodes

```python
# Connect to a remote node
client = RpcClient(
    url="ws://node.example.com:17110",
    network_id="mainnet"
)
```

## Best Practices

1. **Always disconnect**: Use try/finally to ensure disconnection
2. **Check sync status**: Verify the node is synced before operations
3. **Handle errors**: RPC calls can fail, always use try/except
4. **Use async/await**: All RPC methods are async
5. **Connection pooling**: Reuse client instances when possible

## Advanced Usage

### Custom Timeout

```python
client = RpcClient(
    url="ws://127.0.0.1:17110",
    timeout=60  # 60 second timeout
)
```

### Encoding Selection

```python
from kaspa_sdk.rpc.client import Encoding

# Use Borsh encoding (faster, binary)
client = RpcClient(encoding=Encoding.BORSH)

# Use JSON encoding (human-readable)
client = RpcClient(encoding=Encoding.JSON)
```

## Troubleshooting

### Connection Refused

- Check if the node is running
- Verify the RPC port is correct
- Check firewall settings

### Timeout Errors

- Increase timeout parameter
- Check network connectivity
- Verify node is responsive

### Invalid Response

- Ensure node version is compatible
- Check encoding matches node configuration
- Verify request parameters are correct
