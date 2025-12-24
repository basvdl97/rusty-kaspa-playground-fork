# API Reference

Comprehensive API documentation for the Kaspa Python SDK.

## Core Module

### kaspa_sdk.core.network

#### NetworkType

Network type enumeration.

```python
class NetworkType(Enum):
    MAINNET = "mainnet"
    TESTNET = "testnet"
    SIMNET = "simnet"
    DEVNET = "devnet"
```

#### NetworkId

Network identifier with optional version suffix.

**Class Attributes:**
- `MAINNET` - Mainnet identifier
- `TESTNET_10` - Testnet version 10
- `TESTNET_11` - Testnet version 11
- `SIMNET` - Simulation network
- `DEVNET` - Development network

**Properties:**
- `network_type: NetworkType` - Base network type
- `suffix: Optional[int]` - Version number if present
- `default_port: int` - Default RPC port for this network

**Example:**
```python
from kaspa_sdk.core import NetworkId

network = NetworkId.TESTNET_10
print(network.network_type)  # NetworkType.TESTNET
print(network.suffix)  # 10
print(network.default_port)  # 16210
```

## RPC Module

### kaspa_sdk.rpc.encoding

#### Encoding

RPC message encoding format.

```python
class Encoding(Enum):
    BORSH = "borsh"  # Binary encoding (efficient)
    JSON = "json"    # JSON encoding (readable)
    SERDE_JSON = "json"  # Alias for compatibility
```

### kaspa_sdk.rpc.client

#### RpcClient

Async RPC client for Kaspa nodes.

**Constructor:**
```python
RpcClient(
    url: str,
    network_id: NetworkId | str,
    encoding: Encoding = Encoding.BORSH,
    port: Optional[int] = None
)
```

**Methods:**
- `async connect()` - Connect to the node
- `async disconnect()` - Disconnect from the node
- `async get_info()` - Get node information
- `async get_server_info()` - Get server and network info
- `async get_utxos_by_addresses(addresses)` - Get UTXOs for addresses
- `async submit_transaction(transaction)` - Submit a transaction

**Properties:**
- `is_connected: bool` - Connection status

**Example:**
```python
from kaspa_sdk.rpc import RpcClient, Encoding
from kaspa_sdk.core import NetworkId

async with RpcClient(
    url="127.0.0.1",
    network_id=NetworkId.TESTNET_10,
    encoding=Encoding.BORSH
) as client:
    info = await client.get_info()
    print(info)
```

## Wallet Module

### kaspa_sdk.wallet.keys

#### PrivateKey

Secp256k1 private key for Kaspa.

**Constructor:**
```python
PrivateKey(key_data: str | bytes)
```

**Class Methods:**
- `random()` - Generate a random private key

**Methods:**
- `to_public_key()` - Derive public key
- `to_keypair()` - Create keypair
- `to_address(network_type)` - Generate address
- `to_hex()` - Export as hex string

**Example:**
```python
from kaspa_sdk.wallet import PrivateKey
from kaspa_sdk.core import NetworkType

# Generate random key
private_key = PrivateKey.random()

# From hex string
private_key = PrivateKey("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef")

# Derive public key and address
public_key = private_key.to_public_key()
address = private_key.to_address(NetworkType.MAINNET)
```

#### PublicKey

Secp256k1 public key for Kaspa.

**Constructor:**
```python
PublicKey(key_data: str | bytes)
```

**Methods:**
- `to_address(network_type)` - Generate address
- `to_hex()` - Export as hex string

#### Mnemonic

BIP39 mnemonic phrase for key derivation.

**Constructor:**
```python
Mnemonic(phrase: str)
```

**Class Methods:**
- `random(word_count: int = 12)` - Generate random mnemonic

**Properties:**
- `phrase: str` - The mnemonic phrase

**Methods:**
- `to_seed(password: str = "")` - Generate seed
- `to_private_key(account: int = 0, index: int = 0)` - Derive private key

**Example:**
```python
from kaspa_sdk.wallet import Mnemonic

# Generate new mnemonic
mnemonic = Mnemonic.random(word_count=12)
print(mnemonic.phrase)

# Restore from phrase
mnemonic = Mnemonic("legal winner thank year wave sausage worth useful legal winner thank yellow")

# Derive keys
private_key = mnemonic.to_private_key(account=0, index=0)
```

## Utils Module

### kaspa_sdk.utils.conversion

#### Functions

**kaspa_to_sompi(amount)**
Convert KAS to sompi.

```python
sompi = kaspa_to_sompi("1.5")  # Returns 150000000
```

**sompi_to_kaspa(sompi)**
Convert sompi to KAS.

```python
kas = sompi_to_kaspa(150000000)  # Returns Decimal('1.5')
```

**format_kaspa(sompi, decimals=8)**
Format sompi as readable KAS string.

```python
formatted = format_kaspa(150000000, decimals=2)  # Returns "1.50"
```

**Constants:**
- `SOMPI_PER_KASPA` - Number of sompi per KAS (100,000,000)

## Version Module

### kaspa_sdk.version

**Variables:**
- `__version__` - SDK version string
- `__version_info__` - Version as tuple
- `PROTOCOL_VERSION` - Kaspa protocol version
- `MINIMUM_PYTHON_VERSION` - Minimum Python version required

**Functions:**
- `version()` - Get version string
- `version_info()` - Get version tuple

**Example:**
```python
from kaspa_sdk.version import version, PROTOCOL_VERSION

print(f"SDK: {version()}")
print(f"Protocol: {PROTOCOL_VERSION}")
```

## Type Annotations

The SDK uses type hints throughout for better IDE support and type checking:

```python
from typing import Optional
from kaspa_sdk.core import NetworkId
from kaspa_sdk.rpc import RpcClient

def create_client(
    url: str,
    network: NetworkId,
    port: Optional[int] = None
) -> RpcClient:
    return RpcClient(url=url, network_id=network, port=port)
```

## Error Handling

The SDK raises standard Python exceptions:

- `ValueError` - Invalid input values
- `ConnectionError` - Network connection issues
- `NotImplementedError` - Features not yet implemented

**Example:**
```python
from kaspa_sdk.core import NetworkId

try:
    network = NetworkId("invalid-network")
except ValueError as e:
    print(f"Error: {e}")
```

## Async/Await Pattern

The RPC client uses async/await for non-blocking I/O:

```python
import asyncio
from kaspa_sdk.rpc import RpcClient
from kaspa_sdk.core import NetworkId

async def main():
    client = RpcClient(url="127.0.0.1", network_id=NetworkId.TESTNET_10)
    
    try:
        await client.connect()
        info = await client.get_info()
        print(info)
    finally:
        await client.disconnect()

asyncio.run(main())
```

Or use the context manager pattern:

```python
async def main():
    async with RpcClient(url="127.0.0.1", network_id=NetworkId.TESTNET_10) as client:
        info = await client.get_info()
        print(info)

asyncio.run(main())
```
