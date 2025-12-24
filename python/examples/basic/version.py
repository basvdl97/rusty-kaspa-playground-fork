"""
Example: Check SDK version

This example demonstrates how to get the version information
from the Kaspa Python SDK.
"""

from kaspa_sdk import __version__
from kaspa_sdk.version import version, version_info, PROTOCOL_VERSION


def main():
    """Display version information."""
    print("Kaspa Python SDK Version Information")
    print("=" * 50)
    print(f"SDK Version: {__version__}")
    print(f"Version (function): {version()}")
    print(f"Version Info: {version_info()}")
    print(f"Protocol Version: {PROTOCOL_VERSION}")
    print()
    print("This SDK provides Python bindings for the Kaspa blockchain.")


if __name__ == "__main__":
    main()
