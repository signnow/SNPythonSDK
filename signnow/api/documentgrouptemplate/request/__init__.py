"""
DocumentGroupTemplate request classes.
"""

from signnow.api.documentgrouptemplate.request.document_group_template_post_request import (
    DocumentGroupTemplatePostRequest,
)
from signnow.api.documentgrouptemplate.request.document_group_template_recipients_get_request import (
    DocumentGroupTemplateRecipientsGetRequest,
)
from signnow.api.documentgrouptemplate.request.document_group_template_recipients_put_request import (
    DocumentGroupTemplateRecipientsPutRequest,
)

__all__ = [
    "DocumentGroupTemplatePostRequest",
    "DocumentGroupTemplateRecipientsGetRequest",
    "DocumentGroupTemplateRecipientsPutRequest",
]
