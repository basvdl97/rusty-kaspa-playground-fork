# Tests

Test suite for the Kaspa Python SDK.

## Running Tests

### All Tests

```bash
pytest
```

### With Coverage

```bash
pytest --cov=kaspa_sdk --cov-report=html
```

The coverage report will be available in `htmlcov/index.html`.

### Specific Tests

```bash
# Run unit tests only
pytest tests/unit/

# Run integration tests only
pytest tests/integration/

# Run specific test file
pytest tests/unit/test_rpc_client.py

# Run specific test
pytest tests/unit/test_rpc_client.py::TestRpcClient::test_client_creation
```

### Verbose Output

```bash
pytest -v
pytest -vv  # Extra verbose
```

## Test Structure

### Unit Tests

Located in `tests/unit/`, these tests verify individual components without external dependencies:

- `test_package.py` - Package imports and metadata
- `test_helpers.py` - Utility functions
- `test_rpc_client.py` - RPC client initialization and configuration

### Integration Tests

Located in `tests/integration/`, these tests require external services (e.g., running Kaspa node):

- Tests are marked with `@pytest.mark.skip` by default
- Remove skip decorator when you have required services running

## Writing Tests

### Test File Naming

- Test files: `test_*.py`
- Test functions: `test_*`
- Test classes: `Test*`

### Example Test

```python
import pytest
from kaspa_sdk.utils.helpers import kaspa_to_sompi

class TestUnitConversion:
    """Test unit conversion functions."""
    
    def test_kaspa_to_sompi(self):
        """Test converting KAS to Sompi."""
        assert kaspa_to_sompi("1.0") == 100_000_000
        assert kaspa_to_sompi("0.5") == 50_000_000
```

### Async Tests

```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    """Test async function."""
    result = await some_async_function()
    assert result is not None
```

### Fixtures

Use fixtures for common setup:

```python
import pytest
from kaspa_sdk.rpc.client import RpcClient

@pytest.fixture
def rpc_client():
    """Create an RPC client for testing."""
    return RpcClient(url="ws://127.0.0.1:17110")

def test_with_fixture(rpc_client):
    """Test using fixture."""
    assert rpc_client.url == "ws://127.0.0.1:17110"
```

## Test Categories

### Unit Tests

- Fast execution
- No external dependencies
- Test individual functions/methods
- High coverage expected

### Integration Tests

- Require external services
- Test component interactions
- Verify end-to-end workflows
- Marked with appropriate markers

## Running Integration Tests

Integration tests require:

1. **Running Kaspa Node:**

```bash
# Start kaspad with RPC enabled
kaspad --testnet
```

2. **Remove skip markers:**

Remove or modify `@pytest.mark.skip` decorators in integration tests.

3. **Run tests:**

```bash
pytest tests/integration/
```

## Test Markers

Use pytest markers to categorize tests:

```python
@pytest.mark.unit
def test_unit():
    pass

@pytest.mark.integration
def test_integration():
    pass

@pytest.mark.slow
def test_slow():
    pass
```

Run specific markers:

```bash
pytest -m unit
pytest -m integration
pytest -m "not slow"
```

## Coverage Goals

- Overall: >80%
- Core modules (rpc, wallet, transaction): >90%
- Utility functions: 100%

Check coverage:

```bash
pytest --cov=kaspa_sdk --cov-report=term-missing
```

## Continuous Integration

Tests run automatically on:
- Pull requests
- Commits to main branches
- Release tags

## Test Dependencies

- `pytest` - Test framework
- `pytest-asyncio` - Async test support
- `pytest-cov` - Coverage reporting

Install with:

```bash
pip install -e ".[dev]"
```

## Troubleshooting

### Import Errors

If you get import errors, make sure the package is installed:

```bash
pip install -e .
```

### Async Warnings

If you see warnings about async loops, make sure you're using `pytest-asyncio` markers:

```python
@pytest.mark.asyncio
async def test_async():
    pass
```

### Integration Test Failures

- Verify Kaspa node is running
- Check node is synced
- Verify correct network (mainnet/testnet)
- Check RPC port matches configuration

## Contributing Tests

When contributing:

1. Write tests for all new features
2. Update existing tests if behavior changes
3. Ensure all tests pass before submitting PR
4. Aim for high coverage on new code

See [CONTRIBUTING.md](../CONTRIBUTING.md) for more details.
