# Contributing to Kaspa Python SDK

Thank you for your interest in contributing to the Kaspa Python SDK! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to abide by the Kaspa community's code of conduct. Please be respectful and professional in all interactions.

## Getting Started

### Development Setup

1. **Fork and clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/rusty-kaspa.git
cd rusty-kaspa/python
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install in development mode:**

```bash
pip install -e ".[dev]"
```

4. **Install pre-commit hooks (recommended):**

```bash
pip install pre-commit
pre-commit install
```

### Development Workflow

1. **Create a feature branch:**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes**
   - Follow the coding standards (see below)
   - Add tests for new functionality
   - Update documentation as needed

3. **Run tests:**

```bash
pytest
pytest --cov=kaspa_sdk  # With coverage
```

4. **Format and lint code:**

```bash
black kaspa_sdk tests examples
isort kaspa_sdk tests examples
flake8 kaspa_sdk tests examples
mypy kaspa_sdk
```

5. **Commit your changes:**

```bash
git add .
git commit -m "feat: add new feature"
```

6. **Push and create a pull request:**

```bash
git push origin feature/your-feature-name
```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guide
- Maximum line length: 100 characters
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Use [flake8](https://flake8.pycqa.org/) for linting

### Type Hints

- Use type hints for all function signatures
- Support Python 3.8+ type hints
- Use `typing` module for complex types

```python
from typing import Dict, List, Optional, Any

def example_function(
    param1: str,
    param2: Optional[int] = None
) -> Dict[str, Any]:
    """Function with type hints."""
    pass
```

### Docstrings

Use Google-style docstrings:

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

### Testing

- Write tests for all new functionality
- Aim for >80% code coverage
- Use pytest fixtures for common setup
- Separate unit tests from integration tests

```python
import pytest

def test_feature():
    """Test description."""
    # Arrange
    expected = "expected_value"
    
    # Act
    result = function_under_test()
    
    # Assert
    assert result == expected
```

### Async Code

- Use `async/await` for asynchronous operations
- Use `asyncio.run()` for running async code in examples
- Test async code with `pytest-asyncio`

```python
import asyncio

async def async_function():
    """Async function example."""
    await asyncio.sleep(0.1)
    return "result"

# In tests
@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == "result"
```

## Project Structure

```
python/
├── kaspa_sdk/          # Main package
│   ├── __init__.py
│   ├── rpc/            # RPC client
│   ├── wallet/         # Wallet functionality
│   ├── transaction/    # Transaction handling
│   ├── crypto/         # Cryptographic operations
│   └── utils/          # Utilities
├── tests/              # Test suite
│   ├── unit/           # Unit tests
│   └── integration/    # Integration tests
├── examples/           # Example scripts
├── docs/               # Documentation
└── setup.py            # Package setup
```

## What to Contribute

### Priority Areas

1. **Core Functionality:**
   - Complete wallet implementation
   - Transaction signing and creation
   - Cryptographic operations
   - Additional RPC methods

2. **Documentation:**
   - API documentation
   - Tutorials and guides
   - Code examples

3. **Testing:**
   - Unit tests
   - Integration tests
   - Performance tests

4. **Bug Fixes:**
   - Fix reported issues
   - Improve error handling
   - Performance improvements

### Areas That Need Help

- Wallet key derivation (BIP32/BIP39/BIP44)
- Transaction UTXO selection algorithms
- Message signing/verification
- More comprehensive RPC method coverage
- Real-world usage examples

## Pull Request Process

1. **Before submitting:**
   - Ensure all tests pass
   - Update documentation
   - Add/update tests for your changes
   - Format code with Black and isort
   - Check for linting errors

2. **Pull Request description should include:**
   - Summary of changes
   - Related issue numbers
   - Testing performed
   - Breaking changes (if any)

3. **Review process:**
   - At least one maintainer will review
   - Address feedback and comments
   - Keep the PR focused on a single feature/fix

4. **After approval:**
   - Maintainers will merge your PR
   - Thank you for contributing!

## Commit Message Guidelines

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Test additions or changes
- `refactor:` Code refactoring
- `style:` Code style changes (formatting, etc.)
- `chore:` Maintenance tasks

Examples:
```
feat: add transaction signing support
fix: correct address validation for testnet
docs: update API reference for RPC client
test: add unit tests for UTXO selection
```

## Documentation

### Updating Documentation

- Update docstrings when changing functions
- Update README.md for major changes
- Add examples for new features
- Update CHANGELOG.md

### Building Documentation

```bash
cd docs
make html
```

## Testing Guidelines

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=kaspa_sdk --cov-report=html

# Run specific test file
pytest tests/unit/test_rpc_client.py

# Run specific test
pytest tests/unit/test_rpc_client.py::test_client_creation
```

### Writing Tests

- Test file names: `test_*.py`
- Test function names: `test_*`
- Use descriptive names
- One assertion per test (when possible)
- Use fixtures for common setup

## Questions or Issues?

- **Questions:** Ask in [Discord](https://discord.gg/kaspa)
- **Bugs:** Create an [Issue](https://github.com/kaspanet/rusty-kaspa/issues)
- **Discussions:** Use [GitHub Discussions](https://github.com/kaspanet/rusty-kaspa/discussions)

## License

By contributing, you agree that your contributions will be licensed under the ISC License.

## Recognition

Contributors will be recognized in:
- CHANGELOG.md
- GitHub contributors page
- Release notes (for significant contributions)

Thank you for contributing to Kaspa Python SDK! 🎉
