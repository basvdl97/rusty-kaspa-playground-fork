"""
Test package imports and version
"""

import kaspa_sdk
from kaspa_sdk import __version__, __author__, __license__


def test_version():
    """Test version is defined."""
    assert __version__
    assert isinstance(__version__, str)


def test_author():
    """Test author is defined."""
    assert __author__
    assert isinstance(__author__, str)


def test_license():
    """Test license is defined."""
    assert __license__
    assert isinstance(__license__, str)


def test_package_metadata():
    """Test package metadata."""
    assert hasattr(kaspa_sdk, '__title__')
    assert hasattr(kaspa_sdk, '__description__')
    assert hasattr(kaspa_sdk, '__url__')
