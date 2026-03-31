"""
EmbeddedGroupInvite request classes.
"""

from signnow.api.embeddedgroupinvite.request.group_invite_delete_request import (
    GroupInviteDeleteRequest,
)
from signnow.api.embeddedgroupinvite.request.group_invite_link_post_request import (
    GroupInviteLinkPostRequest,
)
from signnow.api.embeddedgroupinvite.request.group_invite_post_request import (
    GroupInvitePostRequest,
)

__all__ = [
    "GroupInvitePostRequest",
    "GroupInviteLinkPostRequest",
    "GroupInviteDeleteRequest",
]
