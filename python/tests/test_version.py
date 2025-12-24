"""
Tests for version module.
"""

import pytest
from kaspa_sdk.version import __version__, version, version_info, PROTOCOL_VERSION


def test_version_string():
    """Test that version is a valid string."""
    assert isinstance(__version__, str)
    assert len(__version__) > 0
    assert version() == __version__


def test_version_info():
    """Test that version_info returns a tuple."""
    info = version_info()
    assert isinstance(info, tuple)
    assert len(info) == 3
    assert all(isinstance(x, int) for x in info)


def test_protocol_version():
    """Test that protocol version is defined."""
    assert isinstance(PROTOCOL_VERSION, str)
    assert len(PROTOCOL_VERSION) > 0


def test_version_format():
    """Test that version follows semver format."""
    parts = __version__.split(".")
    assert len(parts) == 3
    for part in parts:
        assert part.isdigit()
