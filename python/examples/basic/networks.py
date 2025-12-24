"""
Example: Network types

This example demonstrates working with different Kaspa network types.
"""

from kaspa_sdk.core.network import NetworkId, NetworkType


def main():
    """Demonstrate network type usage."""
    print("Kaspa Network Types")
    print("=" * 50)
    
    # Common network identifiers
    networks = [
        NetworkId.MAINNET,
        NetworkId.TESTNET_10,
        NetworkId.TESTNET_11,
        NetworkId.SIMNET,
        NetworkId.DEVNET,
    ]
    
    print("Network Information:")
    for net_str in networks:
        net = NetworkId(net_str)
        print(f"\n  Network: {net}")
        print(f"    Type: {net.network_type.value}")
        print(f"    Suffix: {net.suffix}")
        print(f"    Default Port: {net.default_port}")
    
    print("\n" + "=" * 50)
    print("\nNetwork Type Enum Values:")
    for net_type in NetworkType:
        print(f"  {net_type.name}: {net_type.value}")


if __name__ == "__main__":
    main()
