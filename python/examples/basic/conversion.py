"""
Example: Unit conversion (KAS to Sompi)

This example demonstrates converting between KAS and sompi units.
"""

from kaspa_sdk.utils.conversion import (
    kaspa_to_sompi,
    sompi_to_kaspa,
    format_kaspa,
    SOMPI_PER_KASPA
)


def main():
    """Demonstrate unit conversion."""
    print("Kaspa Unit Conversion Examples")
    print("=" * 50)
    print(f"1 KAS = {SOMPI_PER_KASPA:,} sompi")
    print()
    
    # KAS to sompi conversions
    print("KAS to Sompi:")
    print(f"  1 KAS = {kaspa_to_sompi(1):,} sompi")
    print(f"  0.5 KAS = {kaspa_to_sompi('0.5'):,} sompi")
    print(f"  0.00012 KAS = {kaspa_to_sompi('0.00012'):,} sompi")
    print(f"  0.00000001 KAS = {kaspa_to_sompi('0.00000001'):,} sompi")
    print()
    
    # Sompi to KAS conversions
    print("Sompi to KAS:")
    print(f"  100,000,000 sompi = {sompi_to_kaspa(100_000_000)} KAS")
    print(f"  50,000,000 sompi = {sompi_to_kaspa(50_000_000)} KAS")
    print(f"  12,000 sompi = {sompi_to_kaspa(12_000)} KAS")
    print(f"  1 sompi = {sompi_to_kaspa(1)} KAS")
    print()
    
    # Formatted output
    print("Formatted KAS amounts:")
    print(f"  {format_kaspa(100_000_000)} KAS")
    print(f"  {format_kaspa(50_000_000, decimals=2)} KAS (2 decimals)")
    print(f"  {format_kaspa(12_000, decimals=8)} KAS")


if __name__ == "__main__":
    main()
