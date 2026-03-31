"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict, List, Optional, Union

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="sendFieldInvite",
    url="/document/{document_id}/invite",
    method="post",
    auth="bearer",
    namespace="documentInvite",
    entity="sendInvite",
    content_type="application/json",
)
class SendInvitePostRequest(RequestInterface):
    """
    This class represents a request to send an invite post.
    """

    def __init__(
        self,
        to: Union[List[Dict], Dict],
        from_email: str,
        subject: str,
        message: str,
        email_groups: Optional[Union[List[Dict], Dict]] = None,
        cc: Optional[Union[List[Dict], Dict]] = None,
        cc_step: Optional[Union[List[Dict], Dict]] = None,
        viewers: Optional[Union[List[Dict], Dict]] = None,
        cc_subject: Optional[str] = None,
        cc_message: Optional[str] = None,
    ):
        """
        Constructs a new SendInvitePostRequest.

        Args:
            to: The collection of recipients (list of dicts or dict)
            from_email: The sender of the invite
            subject: The subject of the invite
            message: The message of the invite
            email_groups: The collection of email groups (optional)
            cc: The collection of CC recipients (optional)
            cc_step: The collection of CC steps (optional)
            viewers: The collection of viewers (optional)
            cc_subject: The subject of the CC invite (optional)
            cc_message: The message of the CC invite (optional)
        """
        # Convert to list if it's a single dict
        if isinstance(to, dict):
            self._to = [to]
        else:
            self._to = to or []
        self._from = from_email
        self._subject = subject
        self._message = message
        self._email_groups = email_groups
        self._cc = cc
        self._cc_step = cc_step
        self._viewers = viewers
        self._cc_subject = cc_subject
        self._cc_message = cc_message
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "SendInvitePostRequest":
        """
        Sets the document ID and returns the updated request.

        Args:
            document_id: The ID of the document

        Returns:
            The current SendInvitePostRequest instance
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

    def payload(self) -> Dict[str, Union[str, List, Dict, None]]:
        """
        Returns the payload of the request as a dict.

        Returns:
            A dict containing the payload
        """
        payload: Dict[str, Union[str, List, Dict, None]] = {
            "to": self._to,
            "from": self._from,
            "subject": self._subject,
            "message": self._message,
        }

        if self._email_groups is not None:
            payload["email_groups"] = (
                self._email_groups
                if isinstance(self._email_groups, list)
                else [self._email_groups]
            )
        if self._cc is not None:
            payload["cc"] = self._cc if isinstance(self._cc, list) else [self._cc]
        if self._cc_step is not None:
            payload["cc_step"] = (
                self._cc_step if isinstance(self._cc_step, list) else [self._cc_step]
            )
        if self._viewers is not None:
            payload["viewers"] = (
                self._viewers if isinstance(self._viewers, list) else [self._viewers]
            )
        if self._cc_subject:
            payload["cc_subject"] = self._cc_subject
        if self._cc_message:
            payload["cc_message"] = self._cc_message

        return payload
