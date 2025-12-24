# Kaspa Python SDK Documentation

This directory contains comprehensive documentation for the Kaspa Python SDK.

## Documentation Structure

### API Reference

Complete API documentation for all modules:

- **RPC Module** - WebSocket RPC client and methods
- **Wallet Module** - HD wallet, accounts, and key management
- **Transaction Module** - Transaction creation, signing, and UTXO management
- **Crypto Module** - Cryptographic operations and address handling
- **Utils Module** - Utility functions and constants

### Guides

Step-by-step guides for common tasks:

- **Getting Started** - Installation and basic setup
- **RPC Guide** - Working with the RPC client
- **Wallet Guide** - Creating and managing wallets
- **Transaction Guide** - Creating and sending transactions
- **Network Guide** - Network configuration and switching

## Building Documentation

To build the HTML documentation:

```bash
# Install documentation dependencies
pip install -e ".[dev]"

# Build documentation (requires Sphinx)
cd docs
make html

# View documentation
open _build/html/index.html
```

## Online Documentation

Once published, documentation will be available at:
- [Kaspa Documentation](https://kaspa.aspectron.org/)
- [Python SDK Docs](https://kaspa.aspectron.org/python-sdk/)

## Contributing to Documentation

Contributions to documentation are welcome! Please ensure:

1. Follow Google-style docstrings for Python code
2. Include code examples where appropriate
3. Keep documentation up-to-date with code changes
4. Build and verify HTML output before submitting

## Documentation Standards

### Docstring Format

We use Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of the function.
    
    More detailed description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When invalid input is provided
        
    Example:
        >>> function_name("test", 42)
        True
    """
    pass
```

### Code Examples

All code examples should be:
- Fully functional
- Well-commented
- Follow PEP 8 style guidelines
- Include error handling where appropriate
