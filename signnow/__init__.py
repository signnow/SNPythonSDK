"""
SignNow Python SDK
"""

try:
    from importlib.metadata import version

    __version__ = version("signnow-python-sdk")
except Exception:
    __version__ = "3.0.0"

from signnow.sdk import Sdk
from signnow.core.factory import SdkFactory

__all__ = ["Sdk", "SdkFactory"]
