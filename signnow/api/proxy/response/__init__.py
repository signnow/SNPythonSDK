"""
Proxy response classes.
"""

from signnow.api.proxy.response.proxy_file_response import ProxyFileResponse
from signnow.api.proxy.response.proxy_json_response import ProxyJsonResponse

__all__ = [
    "ProxyJsonResponse",
    "ProxyFileResponse",
]
