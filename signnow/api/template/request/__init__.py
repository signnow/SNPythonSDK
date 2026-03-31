"""
Template request classes.
"""

from signnow.api.template.request.bulk_invite_post_request import BulkInvitePostRequest
from signnow.api.template.request.clone_template_post_request import (
    CloneTemplatePostRequest,
)
from signnow.api.template.request.group_template_get_request import (
    GroupTemplateGetRequest,
)
from signnow.api.template.request.group_template_put_request import (
    GroupTemplatePutRequest,
)
from signnow.api.template.request.routing_details_get_request import (
    RoutingDetailsGetRequest,
)
from signnow.api.template.request.routing_details_post_request import (
    RoutingDetailsPostRequest,
)
from signnow.api.template.request.routing_details_put_request import (
    RoutingDetailsPutRequest,
)
from signnow.api.template.request.template_post_request import TemplatePostRequest

__all__ = [
    "TemplatePostRequest",
    "CloneTemplatePostRequest",
    "BulkInvitePostRequest",
    "RoutingDetailsGetRequest",
    "RoutingDetailsPostRequest",
    "RoutingDetailsPutRequest",
    "GroupTemplateGetRequest",
    "GroupTemplatePutRequest",
]
