"""Version information for Kaspa Python SDK."""

__version__ = "0.1.0"
__version_info__ = tuple(int(x) for x in __version__.split("."))

# SDK version corresponds to the Kaspa protocol version
PROTOCOL_VERSION = "0.13.5"

# Minimum supported Python version
MINIMUM_PYTHON_VERSION = (3, 8)


def version() -> str:
    """
    Get the SDK version string.
    
    Returns:
        str: Version in format "major.minor.patch"
    
    Example:
        >>> from kaspa_sdk import version
        >>> print(version())
        0.1.0
    """
    return __version__


def version_info() -> tuple[int, ...]:
    """
    Get the SDK version as a tuple.
    
    Returns:
        tuple: Version as (major, minor, patch)
    
    Example:
        >>> from kaspa_sdk import version_info
        >>> print(version_info())
        (0, 1, 0)
    """
    return __version_info__
