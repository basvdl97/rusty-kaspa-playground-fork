"""
Example: Get SDK Version

Simple example showing how to import and use the SDK to get version information.
"""

import sys
from pathlib import Path

# Add parent directory to path to allow importing kaspa_sdk
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from kaspa_sdk import __version__, __author__, __license__

def main():
    print(f"Kaspa Python SDK")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
    print(f"License: {__license__}")
    print("\nFor more information, see: https://github.com/kaspanet/rusty-kaspa")

if __name__ == "__main__":
    main()
