"""
Example: Unit Conversion

Demonstrates the conversion between KAS and Sompi units.
"""

import sys
from pathlib import Path

# Add parent directory to path to allow importing kaspa_sdk
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from kaspa_sdk.utils.helpers import (
    kaspa_to_sompi,
    sompi_to_kaspa,
    sompi_to_kaspa_string,
    format_kaspa_amount,
)


def main():
    print("=== Kaspa Unit Conversion Examples ===\n")
    
    # Convert KAS to Sompi
    print("--- KAS to Sompi ---")
    amounts_kas = ["1.0", "0.5", "100.12345678", "0.00000001"]
    
    for amount in amounts_kas:
        sompi = kaspa_to_sompi(amount)
        print(f"{amount} KAS = {sompi:,} Sompi")
    
    # Convert Sompi to KAS
    print("\n--- Sompi to KAS ---")
    amounts_sompi = [100_000_000, 50_000_000, 1, 123_456_789]
    
    for amount in amounts_sompi:
        kas = sompi_to_kaspa(amount)
        print(f"{amount:,} Sompi = {kas} KAS")
    
    # Formatted output
    print("\n--- Formatted Output ---")
    for amount in amounts_sompi:
        formatted = format_kaspa_amount(amount)
        print(f"{amount:,} Sompi = {formatted}")
    
    # String with custom decimal places
    print("\n--- Custom Decimal Places ---")
    amount = 123_456_789
    for decimals in [2, 4, 8]:
        kas_str = sompi_to_kaspa_string(amount, decimals)
        print(f"{amount:,} Sompi = {kas_str} KAS (decimals={decimals})")


if __name__ == "__main__":
    main()
