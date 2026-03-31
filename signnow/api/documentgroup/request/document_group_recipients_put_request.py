"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, List, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="updateDocumentGroupRecipients",
    url="/v2/document-groups/{document_group_id}/recipients",
    method="put",
    auth="bearer",
    namespace="documentGroup",
    entity="documentGroupRecipients",
    content_type="application/json",
)
class DocumentGroupRecipientsPutRequest(RequestInterface):
    """
    Represents a request to update document group recipients.
    """

    def __init__(
        self,
        recipients: Optional[List[Dict[str, Any]]] = None,
        cc: Optional[List[Dict[str, Any]]] = None,
        general_expiration_days: Optional[int] = None,
        general_reminder: Optional[Dict[str, int]] = None,
        order_type: Optional[str] = None,
    ):
        """
        Constructs a new DocumentGroupRecipientsPutRequest.

        Args:
            recipients: The collection of recipients. Optional.
            cc: The collection of cc. Optional.
            general_expiration_days: Number of days before the invite expires. Optional.
            general_reminder: Reminder settings with keys remind_before, remind_repeat,
                remind_after (values in days). Optional.
            order_type: Signing order type. Optional. Possible values:
                at_the_same_time, recipient_order, advanced_order.
        """
        self.recipients = recipients or []
        self.cc = cc or []
        self.general_expiration_days = general_expiration_days
        self.general_reminder = general_reminder
        self.order_type = order_type
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "DocumentGroupRecipientsPutRequest":
        """
        Sets the document group ID in the URI parameters.

        Args:
            document_group_id: The document group ID.

        Returns:
            The current instance of DocumentGroupRecipientsPutRequest.
        """
        self._uri_params["document_group_id"] = document_group_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns a copy of the URI parameters.

        Returns:
            A dictionary containing the URI parameters.
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, Any]:
        """
        Returns a dictionary with the payload of the request.

        Returns:
            A dictionary containing recipients and cc.
        """
        payload: Dict[str, Any] = {}
        if self.recipients:
            payload["recipients"] = self.recipients
        if self.cc:
            payload["cc"] = self.cc
        if self.general_expiration_days is not None:
            payload["general_expiration_days"] = self.general_expiration_days
        if self.general_reminder is not None:
            payload["general_reminder"] = self.general_reminder
        if self.order_type is not None:
            payload["order_type"] = self.order_type
        return payload
