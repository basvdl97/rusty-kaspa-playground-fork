"""
Tests for unit conversion utilities.
"""

import pytest
from decimal import Decimal
from kaspa_sdk.utils.conversion import (
    kaspa_to_sompi,
    sompi_to_kaspa,
    format_kaspa,
    SOMPI_PER_KASPA
)


class TestKaspaToSompi:
    """Tests for kaspa_to_sompi function."""
    
    def test_integer_conversion(self):
        """Test converting integer KAS values."""
        assert kaspa_to_sompi(1) == 100_000_000
        assert kaspa_to_sompi(10) == 1_000_000_000
    
    def test_string_conversion(self):
        """Test converting string KAS values."""
        assert kaspa_to_sompi("1.5") == 150_000_000
        assert kaspa_to_sompi("0.5") == 50_000_000
        assert kaspa_to_sompi("0.00000001") == 1
    
    def test_float_conversion(self):
        """Test converting float KAS values."""
        assert kaspa_to_sompi(1.5) == 150_000_000
        assert kaspa_to_sompi(0.5) == 50_000_000
    
    def test_decimal_conversion(self):
        """Test converting Decimal KAS values."""
        assert kaspa_to_sompi(Decimal("1.5")) == 150_000_000
    
    def test_zero(self):
        """Test zero conversion."""
        assert kaspa_to_sompi(0) == 0
        assert kaspa_to_sompi("0") == 0
    
    def test_negative_raises_error(self):
        """Test that negative values raise ValueError."""
        with pytest.raises(ValueError):
            kaspa_to_sompi(-1)


class TestSompiToKaspa:
    """Tests for sompi_to_kaspa function."""
    
    def test_basic_conversion(self):
        """Test basic sompi to KAS conversion."""
        assert sompi_to_kaspa(100_000_000) == Decimal("1")
        assert sompi_to_kaspa(150_000_000) == Decimal("1.5")
    
    def test_small_amounts(self):
        """Test converting small sompi amounts."""
        assert sompi_to_kaspa(1) == Decimal("0.00000001")
        assert sompi_to_kaspa(100) == Decimal("0.000001")
    
    def test_zero(self):
        """Test zero conversion."""
        assert sompi_to_kaspa(0) == Decimal("0")
    
    def test_negative_raises_error(self):
        """Test that negative values raise ValueError."""
        with pytest.raises(ValueError):
            sompi_to_kaspa(-1)


class TestFormatKaspa:
    """Tests for format_kaspa function."""
    
    def test_default_formatting(self):
        """Test default 8 decimal places."""
        assert format_kaspa(100_000_000) == "1.00000000"
        assert format_kaspa(150_000_000) == "1.50000000"
    
    def test_custom_decimals(self):
        """Test custom decimal places."""
        assert format_kaspa(100_000_000, decimals=2) == "1.00"
        assert format_kaspa(150_000_000, decimals=4) == "1.5000"
    
    def test_small_amounts(self):
        """Test formatting small amounts."""
        assert format_kaspa(1, decimals=8) == "0.00000001"


class TestConstants:
    """Tests for module constants."""
    
    def test_sompi_per_kaspa(self):
        """Test SOMPI_PER_KASPA constant."""
        assert SOMPI_PER_KASPA == 100_000_000
