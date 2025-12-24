"""
Example: RPC Connection

Demonstrates how to connect to a Kaspa node via RPC and retrieve basic information.

Requirements:
- A running Kaspa node (kaspad) with RPC enabled
- Default connection: ws://127.0.0.1:17110
"""

import sys
from pathlib import Path

# Add parent directory to path to allow importing kaspa_sdk
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import asyncio
from kaspa_sdk.rpc.client import RpcClient


async def main():
    # Create RPC client
    # Use default local node on mainnet
    client = RpcClient(
        url="ws://127.0.0.1:17110",
        network_id="mainnet"
    )
    
    print(f"Connecting to {client.url}...")
    
    try:
        # Connect to the node
        await client.connect()
        print("Connected!")
        
        # Get server info
        print("\n--- Server Info ---")
        server_info = await client.get_server_info()
        print(f"Is Synced: {server_info.get('isSynced')}")
        print(f"Virtual DAA Score: {server_info.get('virtualDaaScore')}")
        
        # Get block DAG info
        print("\n--- Block DAG Info ---")
        dag_info = await client.get_block_dag_info()
        print(f"Block Count: {dag_info.get('blockCount')}")
        print(f"Header Count: {dag_info.get('headerCount')}")
        print(f"Tip Hashes: {dag_info.get('tipHashes', [])[:3]}...")
        
        # Get general info
        print("\n--- Node Info ---")
        info = await client.get_info()
        print(f"Server Version: {info.get('serverVersion')}")
        print(f"Is UTC Synced: {info.get('isUtxoIndexed')}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Always disconnect
        await client.disconnect()
        print("\nDisconnected.")


if __name__ == "__main__":
    # For testnet-11, use:
    # client = RpcClient(url="ws://127.0.0.1:17310", network_id="testnet-11")
    
    asyncio.run(main())
