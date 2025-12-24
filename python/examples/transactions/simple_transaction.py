"""
Example: Simple transaction (PLACEHOLDER)

This example will demonstrate creating and sending a basic transaction.
Implementation pending - requires RPC client and wallet functionality.

Expected usage:
    python simple_transaction.py --network testnet-10 --to <address> --amount 0.5
"""

# TODO: Implement after RPC client and wallet are ready
# 
# from kaspa_sdk import RpcClient, PrivateKey, NetworkId
# from kaspa_sdk.utils import kaspa_to_sompi
# 
# async def main():
#     # Connect to node
#     async with RpcClient(
#         url="127.0.0.1",
#         network_id=NetworkId.TESTNET_10
#     ) as client:
#         # Check node is synced
#         server_info = await client.get_server_info()
#         if not server_info.is_synced:
#             print("Node is not synced. Please wait.")
#             return
#         
#         # Create transaction
#         private_key = PrivateKey("your_private_key_here")
#         source_address = private_key.to_address(NetworkType.TESTNET)
#         
#         # Get UTXOs
#         utxos = await client.get_utxos_by_addresses([source_address])
#         
#         # Build transaction
#         transaction = await create_transaction(
#             utxos=utxos.entries,
#             outputs=[{
#                 "address": destination_address,
#                 "amount": kaspa_to_sompi("0.5")
#             }],
#             change_address=source_address
#         )
#         
#         # Sign and submit
#         await transaction.sign([private_key])
#         tx_id = await transaction.submit(client)
#         print(f"Transaction submitted: {tx_id}")


def main():
    """Placeholder main function."""
    print("=" * 60)
    print("Simple Transaction Example (PLACEHOLDER)")
    print("=" * 60)
    print()
    print("This example is not yet implemented.")
    print("It will demonstrate:")
    print("  1. Connecting to a Kaspa node")
    print("  2. Retrieving UTXOs for an address")
    print("  3. Creating a transaction")
    print("  4. Signing the transaction")
    print("  5. Submitting to the network")
    print()
    print("Implementation requires:")
    print("  - RPC client (WebSocket communication)")
    print("  - Wallet functionality (key management)")
    print("  - Transaction builder")
    print("  - Rust bindings via PyO3")


if __name__ == "__main__":
    main()
