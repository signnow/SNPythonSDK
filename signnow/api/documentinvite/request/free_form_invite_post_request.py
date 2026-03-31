"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict, List, Optional, Union

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createFreeFormInvite",
    url="/document/{document_id}/invite",
    method="post",
    auth="bearer",
    namespace="documentInvite",
    entity="freeFormInvite",
    content_type="application/json",
)
class FreeFormInvitePostRequest(RequestInterface):
    """
    This class represents a request to create a free form invite.
    """

    def __init__(
        self,
        to: str,
        from_email: str,
        cc: Optional[Union[List[Dict], Dict]] = None,
        subject: Optional[str] = None,
        message: Optional[str] = None,
        cc_subject: Optional[str] = None,
        cc_message: Optional[str] = None,
        language: Optional[str] = None,
        client_timestamp: Optional[int] = None,
        callback_url: Optional[str] = None,
        is_first_invite_in_sequence: Optional[bool] = None,
        redirect_uri: Optional[str] = None,
        close_redirect_uri: Optional[str] = None,
        redirect_target: Optional[str] = None,
    ):
        """
        Constructs a new FreeFormInvitePostRequest.

        Args:
            to: The recipient of the invite
            from_email: The sender of the invite
            cc: The collection of CC recipients (optional)
            subject: The subject of the invite (optional)
            message: The message of the invite (optional)
            cc_subject: The subject of the CC invite (optional)
            cc_message: The message of the CC invite (optional)
            language: The language of the invite (optional)
            client_timestamp: The client timestamp of the invite (optional)
            callback_url: The callback URL of the invite (optional)
            is_first_invite_in_sequence: Flag indicating if this is the first invite (optional)
            redirect_uri: The redirect URI of the invite (optional)
            close_redirect_uri: The close redirect URI of the invite (optional)
            redirect_target: The redirect target of the invite (optional)
        """
        self._to = to
        self._from = from_email
        self._cc = cc
        self._subject = subject
        self._message = message
        self._cc_subject = cc_subject
        self._cc_message = cc_message
        self._language = language
        self._client_timestamp = client_timestamp
        self._callback_url = callback_url
        self._is_first_invite_in_sequence = is_first_invite_in_sequence
        self._redirect_uri = redirect_uri
        self._close_redirect_uri = close_redirect_uri
        self._redirect_target = redirect_target
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "FreeFormInvitePostRequest":
        """
        Adds a document ID to the URI parameters.

        Args:
            document_id: The ID of the document

        Returns:
            The current FreeFormInvitePostRequest instance
        """
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns the URI parameters for the request.

        Returns:
            A dict containing the URI parameters
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, Union[str, int, bool, List, Dict, None]]:
        """
        Returns a dict containing the payload of the request.

        Returns:
            A dict containing the payload of the request
        """
        payload: Dict[str, Union[str, int, bool, List, Dict, None]] = {
            "to": self._to,
            "from": self._from,
        }

        if self._cc is not None:
            payload["cc"] = self._cc
        if self._subject:
            payload["subject"] = self._subject
        if self._message:
            payload["message"] = self._message
        if self._cc_subject:
            payload["cc_subject"] = self._cc_subject
        if self._cc_message:
            payload["cc_message"] = self._cc_message
        if self._language:
            payload["language"] = self._language
        if self._client_timestamp is not None:
            payload["client_timestamp"] = self._client_timestamp
        if self._callback_url:
            payload["callback_url"] = self._callback_url
        if self._is_first_invite_in_sequence is not None:
            payload["is_first_invite_in_sequence"] = self._is_first_invite_in_sequence
        if self._redirect_uri:
            payload["redirect_uri"] = self._redirect_uri
        if self._close_redirect_uri:
            payload["close_redirect_uri"] = self._close_redirect_uri
        if self._redirect_target:
            payload["redirect_target"] = self._redirect_target

        return payload
