"""
Unit conversion utilities for Kaspa amounts.

Kaspa uses "sompi" as the base unit (similar to satoshi in Bitcoin).
1 KAS = 100,000,000 sompi (10^8)
"""

from decimal import Decimal
from typing import Union

# Sompi per KAS (10^8)
SOMPI_PER_KASPA = 100_000_000


def kaspa_to_sompi(amount: Union[str, float, Decimal, int]) -> int:
    """
    Convert KAS to sompi.
    
    Args:
        amount: Amount in KAS (can be string, float, Decimal, or int)
    
    Returns:
        int: Amount in sompi
    
    Example:
        >>> kaspa_to_sompi("1.5")
        150000000
        >>> kaspa_to_sompi(0.00000001)
        1
    
    Raises:
        ValueError: If amount is negative or invalid
    """
    if isinstance(amount, str):
        amount = Decimal(amount)
    elif isinstance(amount, float):
        amount = Decimal(str(amount))
    elif isinstance(amount, int):
        amount = Decimal(amount)
    elif not isinstance(amount, Decimal):
        raise ValueError(f"Invalid amount type: {type(amount)}")
    
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    
    sompi = int(amount * SOMPI_PER_KASPA)
    return sompi


def sompi_to_kaspa(sompi: int) -> Decimal:
    """
    Convert sompi to KAS.
    
    Args:
        sompi: Amount in sompi
    
    Returns:
        Decimal: Amount in KAS
    
    Example:
        >>> sompi_to_kaspa(150000000)
        Decimal('1.5')
        >>> sompi_to_kaspa(1)
        Decimal('0.00000001')
    
    Raises:
        ValueError: If sompi is negative
    """
    if sompi < 0:
        raise ValueError("Sompi cannot be negative")
    
    kas = Decimal(sompi) / SOMPI_PER_KASPA
    return kas


def format_kaspa(sompi: int, decimals: int = 8) -> str:
    """
    Format sompi as a readable KAS string.
    
    Args:
        sompi: Amount in sompi
        decimals: Number of decimal places to display (default: 8)
    
    Returns:
        str: Formatted KAS amount
    
    Example:
        >>> format_kaspa(150000000)
        '1.50000000'
        >>> format_kaspa(150000000, decimals=2)
        '1.50'
    """
    kas = sompi_to_kaspa(sompi)
    return f"{kas:.{decimals}f}"
