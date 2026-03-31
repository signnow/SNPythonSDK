"""
DocumentGroup request classes.
"""

from signnow.api.documentgroup.request.document_group_delete_request import (
    DocumentGroupDeleteRequest,
)
from signnow.api.documentgroup.request.document_group_get_request import (
    DocumentGroupGetRequest,
)
from signnow.api.documentgroup.request.document_group_post_request import (
    DocumentGroupPostRequest,
)
from signnow.api.documentgroup.request.document_group_recipients_get_request import (
    DocumentGroupRecipientsGetRequest,
)
from signnow.api.documentgroup.request.document_group_recipients_put_request import (
    DocumentGroupRecipientsPutRequest,
)
from signnow.api.documentgroup.request.download_document_group_post_request import (
    DownloadDocumentGroupPostRequest,
)

__all__ = [
    "DocumentGroupGetRequest",
    "DocumentGroupPostRequest",
    "DocumentGroupDeleteRequest",
    "DocumentGroupRecipientsGetRequest",
    "DocumentGroupRecipientsPutRequest",
    "DownloadDocumentGroupPostRequest",
]
