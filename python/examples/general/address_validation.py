"""
Example: Address Validation

Demonstrates address validation for different networks.
"""

import sys
from pathlib import Path

# Add parent directory to path to allow importing kaspa_sdk
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from kaspa_sdk.utils.helpers import validate_address, get_network_prefix


def main():
    print("=== Kaspa Address Validation Examples ===\n")
    
    # Test addresses for different networks
    test_cases = [
        {
            "address": "kaspa:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl",
            "network": "mainnet",
        },
        {
            "address": "kaspatest:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl",
            "network": "testnet-11",
        },
        {
            "address": "kaspa:invalid_address",
            "network": "mainnet",
        },
        {
            "address": "wrongprefix:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl",
            "network": "mainnet",
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        address = test["address"]
        network = test["network"]
        is_valid = validate_address(address, network)
        
        print(f"Test {i}:")
        print(f"  Address: {address}")
        print(f"  Network: {network}")
        print(f"  Valid: {is_valid}")
        print()
    
    # Show network prefixes
    print("\n--- Network Prefixes ---")
    networks = ["mainnet", "testnet-10", "testnet-11", "simnet", "devnet"]
    
    for network in networks:
        prefix = get_network_prefix(network)
        print(f"{network:12s} -> {prefix}")


if __name__ == "__main__":
    main()
