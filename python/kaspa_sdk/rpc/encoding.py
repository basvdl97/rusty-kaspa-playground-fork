"""
Encoding types for RPC communication.

Kaspa RPC supports multiple serialization formats for communication:
- Borsh: Binary encoding (more efficient)
- JSON: Text-based encoding (more readable)
"""

from enum import Enum


class Encoding(Enum):
    """
    RPC message encoding format.
    
    Attributes:
        BORSH: Binary Object Representation Serialization for Hashing
               More efficient but less human-readable
        JSON: JavaScript Object Notation
              Less efficient but human-readable and debuggable
    """
    
    BORSH = "borsh"
    JSON = "json"
    SERDE_JSON = "json"  # Alias for compatibility with WASM SDK
    
    def __str__(self) -> str:
        """String representation of the encoding."""
        return self.value
