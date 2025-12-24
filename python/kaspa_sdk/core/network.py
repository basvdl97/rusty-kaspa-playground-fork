"""
Network type definitions for Kaspa.

Kaspa supports multiple network types for different environments:
- Mainnet: Production network
- Testnet: Testing network (multiple versions)
- Simnet: Simulation network for development
- Devnet: Development network
"""

from enum import Enum
from typing import Optional


class NetworkType(Enum):
    """
    Network type enumeration.
    
    Attributes:
        MAINNET: Production network
        TESTNET: Testing network
        SIMNET: Simulation network
        DEVNET: Development network
    """
    
    MAINNET = "mainnet"
    TESTNET = "testnet"
    SIMNET = "simnet"
    DEVNET = "devnet"


class NetworkId:
    """
    Network identifier with optional suffix for versioned networks.
    
    Examples:
        >>> NetworkId.MAINNET
        NetworkId('mainnet')
        >>> NetworkId.TESTNET_10
        NetworkId('testnet-10')
        >>> NetworkId.TESTNET_11
        NetworkId('testnet-11')
    """
    
    # Common network identifiers
    MAINNET = "mainnet"
    TESTNET_10 = "testnet-10"
    TESTNET_11 = "testnet-11"
    SIMNET = "simnet"
    DEVNET = "devnet"
    
    def __init__(self, network_id: str):
        """
        Initialize a network identifier.
        
        Args:
            network_id: Network identifier string (e.g., "mainnet", "testnet-10")
        
        Raises:
            ValueError: If network_id format is invalid
        """
        self._network_id = network_id
        self._validate()
    
    def _validate(self) -> None:
        """Validate the network identifier format."""
        parts = self._network_id.split("-")
        if parts[0] not in ["mainnet", "testnet", "simnet", "devnet"]:
            raise ValueError(f"Invalid network type: {parts[0]}")
        
        if len(parts) > 1:
            try:
                int(parts[1])
            except ValueError:
                raise ValueError(f"Invalid network suffix: {parts[1]}")
    
    @property
    def network_type(self) -> NetworkType:
        """Get the base network type."""
        network_str = self._network_id.split("-")[0]
        return NetworkType(network_str)
    
    @property
    def suffix(self) -> Optional[int]:
        """Get the network suffix (version number) if present."""
        parts = self._network_id.split("-")
        return int(parts[1]) if len(parts) > 1 else None
    
    @property
    def default_port(self) -> int:
        """
        Get the default RPC port for this network.
        
        Returns:
            int: Default port number
        """
        if self.network_type == NetworkType.MAINNET:
            return 16110
        elif self.network_type == NetworkType.TESTNET:
            return 16210
        elif self.network_type == NetworkType.SIMNET:
            return 16510
        else:  # DEVNET
            return 16610
    
    def __str__(self) -> str:
        """String representation of the network ID."""
        return self._network_id
    
    def __repr__(self) -> str:
        """Developer representation of the network ID."""
        return f"NetworkId('{self._network_id}')"
    
    def __eq__(self, other: object) -> bool:
        """Check equality with another NetworkId."""
        if not isinstance(other, NetworkId):
            return NotImplemented
        return self._network_id == other._network_id
    
    def __hash__(self) -> int:
        """Hash for use in dictionaries and sets."""
        return hash(self._network_id)
