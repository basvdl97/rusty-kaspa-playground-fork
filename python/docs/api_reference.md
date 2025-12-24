# API Reference

Complete API documentation for the Kaspa Python SDK.

## Core Modules

### kaspa_sdk

Main package exports and metadata.

#### Attributes

- `__version__` (str): SDK version number
- `__author__` (str): Package author
- `__license__` (str): License type (ISC)
- `__title__` (str): Package title
- `__description__` (str): Package description
- `__url__` (str): Package URL

---

## kaspa_sdk.rpc

RPC client for communicating with Kaspa nodes.

### RpcClient

WebSocket-based RPC client for Kaspa nodes.

#### Constructor

```python
RpcClient(
    url: str = "ws://127.0.0.1:17110",
    network_id: str = "mainnet",
    encoding: Encoding = Encoding.BORSH,
    timeout: int = 30
)
```

**Parameters:**
- `url` (str): WebSocket URL of the Kaspa node
- `network_id` (str): Network identifier ("mainnet", "testnet-10", "testnet-11")
- `encoding` (Encoding): Message encoding type (BORSH or JSON)
- `timeout` (int): Connection timeout in seconds

#### Properties

- `url` (str): The node URL
- `network_id` (str): The network identifier
- `connected` (bool): Whether the client is currently connected

#### Methods

##### async connect()

Connect to the Kaspa node.

**Raises:**
- `ConnectionError`: If connection fails

##### async disconnect()

Disconnect from the Kaspa node.

##### async get_block_dag_info() -> Dict[str, Any]

Get block DAG information.

**Returns:**
- Dictionary with DAG info including block_count, virtual_daa_score, etc.

##### async get_info() -> Dict[str, Any]

Get node information.

**Returns:**
- Dictionary with node info

##### async get_server_info() -> Dict[str, Any]

Get server information including sync status.

**Returns:**
- Dictionary with server info and is_synced status

##### async get_utxos_by_addresses(addresses: List[str]) -> Dict[str, Any]

Get UTXOs for the given addresses.

**Parameters:**
- `addresses` (List[str]): List of Kaspa addresses

**Returns:**
- Dictionary with entries list of UTXOs

##### async get_balance_by_address(address: str) -> Dict[str, Any]

Get balance for a specific address.

**Parameters:**
- `address` (str): Kaspa address

**Returns:**
- Dictionary with balance information

##### async submit_transaction(transaction: Dict[str, Any]) -> str

Submit a signed transaction to the network.

**Parameters:**
- `transaction` (Dict): Signed transaction object

**Returns:**
- Transaction ID (str)

##### add_event_listener(event_type: Union[str, List[str]], callback: Callable) -> None

Add an event listener.

**Parameters:**
- `event_type` (str or List[str]): Event type(s) to listen for
- `callback` (Callable): Callback function to invoke on event

##### remove_event_listener(event_type: str, callback: Callable) -> None

Remove an event listener.

**Parameters:**
- `event_type` (str): Event type
- `callback` (Callable): Callback function to remove

### Encoding

Enum for message encoding types.

#### Values

- `BORSH`: Binary encoding (faster, more efficient)
- `JSON`: JSON encoding (human-readable)

---

## kaspa_sdk.utils

Utility functions and constants.

### Functions

#### kaspa_to_sompi(amount: Union[str, float, int]) -> int

Convert KAS amount to Sompi.

**Parameters:**
- `amount` (str, float, or int): Amount in KAS

**Returns:**
- Amount in Sompi (int)

**Example:**
```python
>>> kaspa_to_sompi("1.5")
150000000
```

#### sompi_to_kaspa(amount: int) -> float

Convert Sompi amount to KAS.

**Parameters:**
- `amount` (int): Amount in Sompi

**Returns:**
- Amount in KAS (float)

**Example:**
```python
>>> sompi_to_kaspa(150000000)
1.5
```

#### sompi_to_kaspa_string(amount: int, decimal_places: int = 8) -> str

Convert Sompi amount to KAS string with specified decimal places.

**Parameters:**
- `amount` (int): Amount in Sompi
- `decimal_places` (int): Number of decimal places (default: 8)

**Returns:**
- Amount in KAS as string

#### format_kaspa_amount(amount: int, include_symbol: bool = True) -> str

Format a Sompi amount as a human-readable KAS string.

**Parameters:**
- `amount` (int): Amount in Sompi
- `include_symbol` (bool): Whether to include "KAS" suffix

**Returns:**
- Formatted string

#### validate_address(address: str, network_id: str = "mainnet") -> bool

Validate a Kaspa address format.

**Parameters:**
- `address` (str): Kaspa address to validate
- `network_id` (str): Network ID to validate against

**Returns:**
- True if valid, False otherwise

#### get_network_prefix(network_id: str) -> str

Get the address prefix for a network.

**Parameters:**
- `network_id` (str): Network identifier

**Returns:**
- Address prefix (str)

**Raises:**
- `ValueError`: If network_id is invalid

#### get_rpc_url(host: str = "127.0.0.1", network_id: str = "mainnet") -> str

Construct RPC URL for a given host and network.

**Parameters:**
- `host` (str): Host address (default: "127.0.0.1")
- `network_id` (str): Network identifier (default: "mainnet")

**Returns:**
- WebSocket RPC URL (str)

### Constants

#### SOMPI_PER_KASPA

Number of Sompi in one KAS (100,000,000).

#### NETWORKS

Dictionary of network configurations with the following structure:

```python
{
    "network_id": {
        "name": str,
        "prefix": str,
        "default_port": int,
        "rpc_port": int,
    }
}
```

Available networks:
- `mainnet`
- `testnet-10`
- `testnet-11`
- `simnet`
- `devnet`

#### BIP32_HARDENED_BIT

BIP32 hardened derivation bit (0x80000000).

#### BIP44_PURPOSE

BIP44 purpose field (44).

#### BIP44_COIN_TYPE

Kaspa coin type for BIP44 (111111).

---

## kaspa_sdk.wallet

Wallet management functionality (Coming Soon).

### Wallet

Main wallet class for managing accounts and keys.

*Documentation will be added when wallet implementation is complete.*

### Account

Individual account within a wallet.

*Documentation will be added when wallet implementation is complete.*

### Mnemonic

BIP39 mnemonic generation and validation.

*Documentation will be added when wallet implementation is complete.*

---

## kaspa_sdk.transaction

Transaction handling functionality (Coming Soon).

### Transaction

Transaction creation and manipulation.

*Documentation will be added when transaction implementation is complete.*

---

## kaspa_sdk.crypto

Cryptographic operations (Coming Soon).

### PrivateKey

Private key operations.

*Documentation will be added when crypto implementation is complete.*

### PublicKey

Public key operations.

*Documentation will be added when crypto implementation is complete.*

### Address

Address generation and validation.

*Documentation will be added when crypto implementation is complete.*

---

## Error Handling

All async methods can raise the following exceptions:

- `ConnectionError`: Connection-related errors
- `RuntimeError`: Runtime errors (e.g., not connected)
- `ValueError`: Invalid parameter values
- `Exception`: General RPC errors

Always use try/except blocks when calling async methods:

```python
try:
    await client.connect()
    result = await client.get_info()
except ConnectionError as e:
    print(f"Connection failed: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    if client.connected:
        await client.disconnect()
```

---

## Type Hints

The SDK uses type hints throughout. For best IDE support, use Python 3.8+ and a type-aware editor like VS Code with Pylance.

Example with type hints:

```python
from typing import Dict, Any
from kaspa_sdk.rpc.client import RpcClient

async def get_node_info(client: RpcClient) -> Dict[str, Any]:
    info: Dict[str, Any] = await client.get_info()
    return info
```
