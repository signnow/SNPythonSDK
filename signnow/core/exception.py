"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Optional


class SignNowApiException(Exception):
    """
    This class represents an exception that is thrown when an error occurs in the SignNow API.
    """

    def __init__(
        self,
        message: str,
        endpoint: Optional[str] = None,
        payload: Optional[str] = None,
        response: Optional[str] = None,
        response_code: Optional[int] = None,
        cause: Optional[Exception] = None,
    ):
        """
        Constructs a new SignNowApiException.

        Args:
            message: The detail message
            endpoint: The endpoint that was called when the exception occurred
            payload: The payload that was sent when the exception occurred
            response: The response that was received when the exception occurred
            response_code: The HTTP status code that was received when the exception occurred
            cause: The cause exception
        """
        super().__init__(message)
        self.endpoint = endpoint
        self.payload = payload
        self.response = response
        self.response_code = response_code
        self.cause = cause

    def __str__(self) -> str:
        """Returns the detail message string of this exception."""
        parts = [super().__str__()]
        if self.endpoint:
            parts.append(f"Endpoint: {self.endpoint}")
        parts.append(f"Status: {self.response_code if self.response_code else '?'}")
        if self.response:
            parts.append(f"Response: {self.response}")
        if self.payload:
            parts.append(f"Request: {self.payload}")
        if self.cause:
            parts.append(f"Cause: {str(self.cause)}")
        return "\n".join(parts)
