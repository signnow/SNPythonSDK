"""
EmbeddedInvite response classes.
"""

from signnow.api.embeddedinvite.response.document_invite_delete_response import (
    DocumentInviteDeleteResponse,
)
from signnow.api.embeddedinvite.response.document_invite_link_post_response import (
    DocumentInviteLinkPostResponse,
)
from signnow.api.embeddedinvite.response.document_invite_post_response import (
    DocumentInvitePostResponse,
)

__all__ = [
    "DocumentInvitePostResponse",
    "DocumentInviteLinkPostResponse",
    "DocumentInviteDeleteResponse",
]
