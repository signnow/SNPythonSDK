"""
DocumentGroupTemplate response classes.
"""

from signnow.api.documentgrouptemplate.response.document_group_template_post_response import (
    DocumentGroupTemplatePostResponse,
)
from signnow.api.documentgrouptemplate.response.document_group_template_recipients_get_response import (
    DocumentGroupTemplateRecipientsGetResponse,
)
from signnow.api.documentgrouptemplate.response.document_group_template_recipients_put_response import (
    DocumentGroupTemplateRecipientsPutResponse,
)

__all__ = [
    "DocumentGroupTemplatePostResponse",
    "DocumentGroupTemplateRecipientsGetResponse",
    "DocumentGroupTemplateRecipientsPutResponse",
]
