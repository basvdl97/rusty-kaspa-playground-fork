"""
Unit tests for utility helpers
"""

import pytest
from kaspa_sdk.utils.helpers import (
    kaspa_to_sompi,
    sompi_to_kaspa,
    sompi_to_kaspa_string,
    format_kaspa_amount,
    validate_address,
    get_network_prefix,
    get_rpc_url,
)
from kaspa_sdk.utils.constants import SOMPI_PER_KASPA


class TestUnitConversion:
    """Test unit conversion functions."""
    
    def test_kaspa_to_sompi_string(self):
        """Test converting KAS string to Sompi."""
        assert kaspa_to_sompi("1.0") == SOMPI_PER_KASPA
        assert kaspa_to_sompi("0.5") == SOMPI_PER_KASPA // 2
        assert kaspa_to_sompi("2.0") == SOMPI_PER_KASPA * 2
    
    def test_kaspa_to_sompi_float(self):
        """Test converting KAS float to Sompi."""
        assert kaspa_to_sompi(1.0) == SOMPI_PER_KASPA
        assert kaspa_to_sompi(0.00000001) == 1
    
    def test_kaspa_to_sompi_int(self):
        """Test converting KAS int to Sompi."""
        assert kaspa_to_sompi(1) == SOMPI_PER_KASPA
        assert kaspa_to_sompi(10) == SOMPI_PER_KASPA * 10
    
    def test_sompi_to_kaspa(self):
        """Test converting Sompi to KAS."""
        assert sompi_to_kaspa(SOMPI_PER_KASPA) == 1.0
        assert sompi_to_kaspa(SOMPI_PER_KASPA // 2) == 0.5
        assert sompi_to_kaspa(1) == 0.00000001
    
    def test_sompi_to_kaspa_string(self):
        """Test converting Sompi to KAS string."""
        result = sompi_to_kaspa_string(SOMPI_PER_KASPA)
        assert result == "1.00000000"
        
        result = sompi_to_kaspa_string(SOMPI_PER_KASPA, decimal_places=2)
        assert result == "1.00"
    
    def test_format_kaspa_amount(self):
        """Test formatting Sompi amount."""
        result = format_kaspa_amount(SOMPI_PER_KASPA)
        assert "KAS" in result
        assert "1.00000000" in result
        
        result = format_kaspa_amount(SOMPI_PER_KASPA, include_symbol=False)
        assert "KAS" not in result


class TestAddressValidation:
    """Test address validation functions."""
    
    def test_validate_address_mainnet(self):
        """Test validating mainnet addresses."""
        # Valid format (length check only in this stub)
        valid_address = "kaspa:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl"
        assert validate_address(valid_address, "mainnet") is True
    
    def test_validate_address_testnet(self):
        """Test validating testnet addresses."""
        valid_address = "kaspatest:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl"
        assert validate_address(valid_address, "testnet-11") is True
    
    def test_validate_address_invalid_prefix(self):
        """Test validating address with wrong prefix."""
        invalid_address = "wrongprefix:qz7ulu4c25dh7fzec8uehs4cj4j8z8mu88xqv8cxyj5w5keu7k8vxd5yg39vl"
        assert validate_address(invalid_address, "mainnet") is False
    
    def test_validate_address_too_short(self):
        """Test validating address that's too short."""
        invalid_address = "kaspa:short"
        assert validate_address(invalid_address, "mainnet") is False
    
    def test_validate_address_no_colon(self):
        """Test validating address without colon separator."""
        invalid_address = "kaspa_no_colon_here"
        assert validate_address(invalid_address, "mainnet") is False


class TestNetworkHelpers:
    """Test network helper functions."""
    
    def test_get_network_prefix_mainnet(self):
        """Test getting mainnet prefix."""
        assert get_network_prefix("mainnet") == "kaspa"
    
    def test_get_network_prefix_testnet(self):
        """Test getting testnet prefix."""
        assert get_network_prefix("testnet-11") == "kaspatest"
    
    def test_get_network_prefix_invalid(self):
        """Test getting prefix for invalid network."""
        with pytest.raises(ValueError):
            get_network_prefix("invalid-network")
    
    def test_get_rpc_url_default(self):
        """Test getting default RPC URL."""
        url = get_rpc_url()
        assert url == "ws://127.0.0.1:17110"
    
    def test_get_rpc_url_testnet(self):
        """Test getting testnet RPC URL."""
        url = get_rpc_url(network_id="testnet-11")
        assert url == "ws://127.0.0.1:17310"
    
    def test_get_rpc_url_custom_host(self):
        """Test getting RPC URL with custom host."""
        url = get_rpc_url(host="example.com")
        assert url == "ws://example.com:17110"
    
    def test_get_rpc_url_invalid_network(self):
        """Test getting RPC URL for invalid network."""
        with pytest.raises(ValueError):
            get_rpc_url(network_id="invalid-network")
