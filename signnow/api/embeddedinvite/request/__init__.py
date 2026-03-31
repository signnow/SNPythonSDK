"""
EmbeddedInvite request classes.
"""

from signnow.api.embeddedinvite.request.document_invite_delete_request import (
    DocumentInviteDeleteRequest,
)
from signnow.api.embeddedinvite.request.document_invite_link_post_request import (
    DocumentInviteLinkPostRequest,
)
from signnow.api.embeddedinvite.request.document_invite_post_request import (
    DocumentInvitePostRequest,
)

__all__ = [
    "DocumentInvitePostRequest",
    "DocumentInviteLinkPostRequest",
    "DocumentInviteDeleteRequest",
]
