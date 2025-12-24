"""
Tests for network module.
"""

import pytest
from kaspa_sdk.core.network import NetworkId, NetworkType


class TestNetworkType:
    """Tests for NetworkType enum."""
    
    def test_network_types_exist(self):
        """Test that all network types are defined."""
        assert NetworkType.MAINNET.value == "mainnet"
        assert NetworkType.TESTNET.value == "testnet"
        assert NetworkType.SIMNET.value == "simnet"
        assert NetworkType.DEVNET.value == "devnet"


class TestNetworkId:
    """Tests for NetworkId class."""
    
    def test_common_networks(self):
        """Test common network identifiers."""
        assert NetworkId.MAINNET == "mainnet"
        assert NetworkId.TESTNET_10 == "testnet-10"
        assert NetworkId.TESTNET_11 == "testnet-11"
    
    def test_network_creation(self):
        """Test creating NetworkId instances."""
        net = NetworkId("mainnet")
        assert str(net) == "mainnet"
        
        net = NetworkId("testnet-10")
        assert str(net) == "testnet-10"
    
    def test_network_type_property(self):
        """Test network_type property."""
        net = NetworkId("mainnet")
        assert net.network_type == NetworkType.MAINNET
        
        net = NetworkId("testnet-10")
        assert net.network_type == NetworkType.TESTNET
    
    def test_suffix_property(self):
        """Test suffix property."""
        net = NetworkId("mainnet")
        assert net.suffix is None
        
        net = NetworkId("testnet-10")
        assert net.suffix == 10
    
    def test_default_ports(self):
        """Test default port assignments."""
        assert NetworkId("mainnet").default_port == 16110
        assert NetworkId("testnet-10").default_port == 16210
        assert NetworkId("simnet").default_port == 16510
        assert NetworkId("devnet").default_port == 16610
    
    def test_invalid_network_type(self):
        """Test that invalid network types raise ValueError."""
        with pytest.raises(ValueError):
            NetworkId("invalid")
    
    def test_invalid_suffix(self):
        """Test that invalid suffixes raise ValueError."""
        with pytest.raises(ValueError):
            NetworkId("testnet-abc")
    
    def test_equality(self):
        """Test NetworkId equality."""
        net1 = NetworkId("testnet-10")
        net2 = NetworkId("testnet-10")
        net3 = NetworkId("testnet-11")
        
        assert net1 == net2
        assert net1 != net3
    
    def test_repr(self):
        """Test string representation."""
        net = NetworkId("testnet-10")
        assert repr(net) == "NetworkId('testnet-10')"
        assert str(net) == "testnet-10"
