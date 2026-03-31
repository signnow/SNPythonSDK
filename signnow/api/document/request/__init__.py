"""
Document request models
"""

from signnow.api.document.request.document_get_request import DocumentGetRequest
from signnow.api.document.request.document_post_request import DocumentPostRequest
from signnow.api.document.request.document_delete_request import DocumentDeleteRequest
from signnow.api.document.request.document_download_get_request import (
    DocumentDownloadGetRequest,
)
from signnow.api.document.request.document_history_get_request import (
    DocumentHistoryGetRequest,
)
from signnow.api.document.request.document_move_post_request import (
    DocumentMovePostRequest,
)
from signnow.api.document.request.document_merge_post_request import (
    DocumentMergePostRequest,
)
from signnow.api.document.request.fields_get_request import FieldsGetRequest
from signnow.api.document.request.field_extract_post_request import (
    FieldExtractPostRequest,
)
from signnow.api.document.request.document_put_request import DocumentPutRequest
from signnow.api.document.request.document_download_link_post_request import (
    DocumentDownloadLinkPostRequest,
)

__all__ = [
    "DocumentGetRequest",
    "DocumentPostRequest",
    "DocumentPutRequest",
    "DocumentDeleteRequest",
    "DocumentDownloadGetRequest",
    "DocumentDownloadLinkPostRequest",
    "DocumentHistoryGetRequest",
    "DocumentMovePostRequest",
    "DocumentMergePostRequest",
    "FieldsGetRequest",
    "FieldExtractPostRequest",
]
