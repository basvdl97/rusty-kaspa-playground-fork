# Development Guide

Guide for developing and contributing to the Kaspa Python SDK.

## Setup Development Environment

### Prerequisites

- Python 3.8 or higher
- pip and virtualenv
- Git
- (Future) Rust toolchain for building native extensions

### Clone and Install

```bash
# Clone repository
git clone https://github.com/kaspanet/rusty-kaspa.git
cd rusty-kaspa/python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e ".[dev]"
```

## Project Structure

```
python/
├── kaspa_sdk/          # Main package
│   ├── __init__.py
│   ├── version.py
│   ├── core/           # Core primitives
│   ├── rpc/            # RPC client
│   ├── wallet/         # Wallet functionality
│   └── utils/          # Utilities
├── examples/           # Example scripts
│   ├── basic/
│   ├── transactions/
│   └── wallet/
├── tests/              # Test suite
├── docs/               # Documentation
├── pyproject.toml      # Project configuration
└── README.md           # Package documentation
```

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/test_network.py
```

### Run with Coverage

```bash
pytest --cov=kaspa_sdk --cov-report=html
# View coverage report in htmlcov/index.html
```

### Run Specific Test

```bash
pytest tests/test_network.py::TestNetworkId::test_network_creation
```

## Code Quality

### Format Code

```bash
# Format with black
black kaspa_sdk tests examples

# Check formatting without changes
black --check kaspa_sdk tests examples
```

### Lint Code

```bash
# Run ruff linter
ruff check kaspa_sdk tests examples

# Auto-fix issues
ruff check --fix kaspa_sdk tests examples
```

### Type Checking

```bash
# Run mypy type checker
mypy kaspa_sdk
```

### Run All Checks

```bash
# Format, lint, and type check
black kaspa_sdk tests examples
ruff check kaspa_sdk tests examples
mypy kaspa_sdk
pytest
```

## Writing Tests

### Test Structure

Tests should be organized by module:

```python
# tests/test_module.py
import pytest
from kaspa_sdk.module import SomeClass

class TestSomeClass:
    """Tests for SomeClass."""
    
    def test_basic_functionality(self):
        """Test basic functionality."""
        obj = SomeClass()
        assert obj.method() == expected_value
    
    def test_error_handling(self):
        """Test error handling."""
        with pytest.raises(ValueError):
            SomeClass(invalid_param)
```

### Async Tests

```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    """Test async function."""
    result = await async_function()
    assert result is not None
```

### Fixtures

```python
@pytest.fixture
def sample_network():
    """Provide a sample network for testing."""
    return NetworkId.TESTNET_10

def test_with_fixture(sample_network):
    """Test using fixture."""
    assert sample_network.network_type == NetworkType.TESTNET
```

## Documentation

### Docstring Style

Use Google-style docstrings:

```python
def function(param1: str, param2: int) -> bool:
    """
    Short description of function.
    
    Longer description if needed, explaining the function's
    behavior and any important details.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param1 is invalid
    
    Example:
        >>> function("test", 42)
        True
    """
    pass
```

### Type Hints

Always use type hints:

```python
from typing import Optional, List, Dict

def process_data(
    data: List[Dict[str, int]],
    config: Optional[str] = None
) -> Dict[str, int]:
    """Process data and return result."""
    pass
```

## Git Workflow

### Branch Naming

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `test/description` - Test additions/fixes

### Commit Messages

Use clear, descriptive commit messages:

```
Short summary (50 chars or less)

More detailed explanation if needed. Wrap at 72 characters.
Explain what and why, not how.

- Bullet points are okay
- Use present tense ("Add feature" not "Added feature")
```

### Pull Request Process

1. Create a feature branch
2. Make changes with tests
3. Run all quality checks
4. Push and create PR
5. Address review feedback

## Building Native Extensions (Future)

When Rust bindings are added:

### Install Rust

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Build Extensions

```bash
# Install maturin
pip install maturin

# Build in development mode
maturin develop

# Build release
maturin build --release
```

## Adding New Features

### 1. Plan the Feature

- Review existing WASM SDK implementation
- Design Python API
- Consider async/sync requirements
- Plan tests

### 2. Implement

- Add type definitions
- Implement placeholder/pure Python version
- Write comprehensive tests
- Add documentation

### 3. Add Tests

- Unit tests for new functionality
- Integration tests if applicable
- Edge case coverage

### 4. Document

- Add docstrings
- Update API reference
- Add usage examples
- Update README if needed

## Release Process

### Version Bump

Update version in:
- `pyproject.toml`
- `kaspa_sdk/version.py`

### Build Package

```bash
# Build source and wheel distributions
python -m build
```

### Publish (Maintainers Only)

```bash
# Test PyPI
twine upload --repository testpypi dist/*

# Production PyPI
twine upload dist/*
```

## Debugging

### Print Debugging

```python
import sys
print(f"Debug: {variable}", file=sys.stderr)
```

### PDB Debugger

```python
import pdb; pdb.set_trace()
```

### Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Debug message")
```

## Resources

- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [pytest Documentation](https://docs.pytest.org/)
- [Black Code Style](https://black.readthedocs.io/)
- [Ruff Linter](https://github.com/astral-sh/ruff)
- [PyO3 Guide](https://pyo3.rs/) (for Rust bindings)

## Getting Help

- Check existing issues on GitHub
- Ask in Discord #development channel
- Review WASM SDK for reference implementation
