"""
Helper Functions

Common utility functions for the SDK.
"""

from typing import Union
from kaspa_sdk.utils.constants import SOMPI_PER_KASPA, NETWORKS


def kaspa_to_sompi(amount: Union[str, float, int]) -> int:
    """
    Convert KAS amount to Sompi.
    
    Args:
        amount: Amount in KAS (can be string, float, or int)
        
    Returns:
        Amount in Sompi (int)
        
    Example:
        >>> kaspa_to_sompi("1.5")
        150000000
        >>> kaspa_to_sompi(0.00000001)
        1
    """
    if isinstance(amount, str):
        amount = float(amount)
    return int(amount * SOMPI_PER_KASPA)


def sompi_to_kaspa(amount: int) -> float:
    """
    Convert Sompi amount to KAS.
    
    Args:
        amount: Amount in Sompi
        
    Returns:
        Amount in KAS (float)
        
    Example:
        >>> sompi_to_kaspa(150000000)
        1.5
        >>> sompi_to_kaspa(1)
        1e-08
    """
    return amount / SOMPI_PER_KASPA


def sompi_to_kaspa_string(amount: int, decimal_places: int = 8) -> str:
    """
    Convert Sompi amount to KAS string with specified decimal places.
    
    Args:
        amount: Amount in Sompi
        decimal_places: Number of decimal places (default: 8)
        
    Returns:
        Amount in KAS as string
        
    Example:
        >>> sompi_to_kaspa_string(150000000)
        '1.50000000'
        >>> sompi_to_kaspa_string(150000000, 2)
        '1.50'
    """
    kas = sompi_to_kaspa(amount)
    return f"{kas:.{decimal_places}f}"


def validate_address(address: str, network_id: str = "mainnet") -> bool:
    """
    Validate a Kaspa address format.
    
    Args:
        address: Kaspa address to validate
        network_id: Network ID to validate against
        
    Returns:
        True if valid, False otherwise
        
    Example:
        >>> validate_address("kaspa:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl")
        True
    """
    if not address:
        return False
    
    # Get network prefix
    network = NETWORKS.get(network_id)
    if not network:
        return False
    
    expected_prefix = network["prefix"]
    
    # Check if address starts with correct prefix
    if not address.startswith(f"{expected_prefix}:"):
        return False
    
    # Basic length check (more detailed validation would be in crypto.address module)
    parts = address.split(":")
    if len(parts) != 2:
        return False
    
    payload = parts[1]
    # Kaspa addresses are typically 61-63 characters in the payload
    if len(payload) < 50 or len(payload) > 70:
        return False
    
    return True


def format_kaspa_amount(amount: int, include_symbol: bool = True) -> str:
    """
    Format a Sompi amount as a human-readable KAS string.
    
    Args:
        amount: Amount in Sompi
        include_symbol: Whether to include "KAS" suffix
        
    Returns:
        Formatted string
        
    Example:
        >>> format_kaspa_amount(150000000)
        '1.50000000 KAS'
        >>> format_kaspa_amount(150000000, include_symbol=False)
        '1.50000000'
    """
    kas_str = sompi_to_kaspa_string(amount)
    if include_symbol:
        return f"{kas_str} KAS"
    return kas_str


def get_network_prefix(network_id: str) -> str:
    """
    Get the address prefix for a network.
    
    Args:
        network_id: Network identifier
        
    Returns:
        Address prefix
        
    Raises:
        ValueError: If network_id is invalid
        
    Example:
        >>> get_network_prefix("mainnet")
        'kaspa'
        >>> get_network_prefix("testnet-11")
        'kaspatest'
    """
    network = NETWORKS.get(network_id)
    if not network:
        raise ValueError(f"Invalid network_id: {network_id}")
    return network["prefix"]


def get_rpc_url(host: str = "127.0.0.1", network_id: str = "mainnet") -> str:
    """
    Construct RPC URL for a given host and network.
    
    Args:
        host: Host address (default: "127.0.0.1")
        network_id: Network identifier (default: "mainnet")
        
    Returns:
        WebSocket RPC URL
        
    Example:
        >>> get_rpc_url()
        'ws://127.0.0.1:17110'
        >>> get_rpc_url("example.com", "testnet-11")
        'ws://example.com:17310'
    """
    network = NETWORKS.get(network_id)
    if not network:
        raise ValueError(f"Invalid network_id: {network_id}")
    
    port = network["rpc_port"]
    return f"ws://{host}:{port}"
