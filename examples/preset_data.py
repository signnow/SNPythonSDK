"""
Preset data for examples.

This file contains placeholder/test data for examples. Replace placeholder IDs
with real values from your SignNow account when running examples against the API.
"""

from pathlib import Path

# Base directory for examples
EXAMPLES_DIR = Path(__file__).parent

# =============================================================================
# Bearer token (empty string = SDK will create a new token from .env credentials)
# =============================================================================
PRESET_BEARER_TOKEN = ""

# =============================================================================
# Document IDs (replace with real document IDs from your account)
# =============================================================================
# Used in: document_group_recipients_example, document_group_template_recipients_example
# (document inside a group for recipients PUT request)
PRESET_DOCUMENT_ID = "feae4f8dd6b9455d9572906a3b5436e81f8fc8f2"
# Used in: signing_link_example (document for creating a public signing link)
PRESET_DOCUMENT_ID_2 = "05fbed799231d85cf3471121ecd6a4221f9c5610"
PRESET_DOCUMENT_ID_3 = "b2072009b7e0427dba1f6de56df4812da5d8eb9c"

# =============================================================================
# Template ID used in: bulk_invite_example (template with roles matching CSV columns)
# =============================================================================
PRESET_TEMPLATE_ID = "e2e913db4ba9815a31c8a28a196b7df96fe1cc46"

# =============================================================================
# Folder IDs (replace with real folder IDs from your account)
# =============================================================================
# Used in: folder_example (list folder documents)
PRESET_FOLDER_ID = "14f2b0157ce3cb455a2d8031ccc1fc08bd32f8b5"
# Used in: bulk_invite_example (destination folder for cloned templates)
PRESET_FOLDER_ID_2 = "3073f8da73b9a5328f95ccc55a912e3f46da2d94"
# Used in: document_group_template_example (folder for new group from template)
PRESET_FOLDER_ID_3 = "5d66ca4accdd4ab28f8b2c71001093b5cb3bcb8b"

# =============================================================================
# Test file paths
# =============================================================================
TEST_DOCUMENT_PDF = EXAMPLES_DIR / "test_document.pdf"
TEST_BULK_INVITE_CSV = EXAMPLES_DIR / "test_bulk_invite.csv"

# =============================================================================
# Signer information (use valid email for invite examples)
# =============================================================================
PRESET_SIGNER_EMAIL = "signer@example.com"
PRESET_SIGNER_ROLE = "Signer"
PRESET_SIGNER_NAME = "Test Signer"

# =============================================================================
# Document group settings
# =============================================================================
PRESET_GROUP_NAME = "Test Document Group"
PRESET_DOCUMENT_NAME = "test_document"
PRESET_TEMPLATE_NAME = "test_sdk_template"
# Document group ID (used in: download_document_group_example, document_group_recipients_example)
PRESET_DOCUMENT_GROUP_ID = "4a9b8be64589459c82ff8a5c19ceafec12941c92"
# Template group ID (used in: document_group_template_example, document_group_template_recipients_example)
PRESET_TEMPLATE_GROUP_ID = "5d66ca4accdd4ab28f8b2c71001093b5cb3bcb8a"
# Document IDs order for download_document_group_example (order in merged zip)
PRESET_DOCUMENT_GROUP_DOWNLOAD_ORDER = [
    "05fbed799231d85cf3471121ecd6a4221f9c5610",
    "9a3b1e4f0c2d7a8e5f6b9c1d3e0a4b7c8f2d6a9e",
]
# Document ID within a group for recipients PUT (document_group_recipients_example)
PRESET_DG_RECIPIENT_DOCUMENT_ID = "bf8e821c17814b7a82a8d08d6591119173b079e3"
# Document ID within a template group for recipients PUT (document_group_template_recipients_example)
PRESET_DGT_RECIPIENT_DOCUMENT_ID = "8033ce7afe1b3ab08f8b3c71831093b55b4beb21"
# Document group ID for recipients GET/PUT (document_group_recipients_example)
PRESET_DG_RECIPIENTS_GROUP_ID = "6336ce5aeedd4ab28f8b2c71831093b5cb4bcb2c"
# Template group ID for recipients GET/PUT (document_group_template_recipients_example)
PRESET_DGT_RECIPIENTS_GROUP_ID = "5d66ca4accdd4ab28f8b2c71001093b5cb3bcb8b"

# =============================================================================
# User ID (webhook_example entity_id; get from user_info_example output: response.id)
# =============================================================================
PRESET_USER_ID = "f2e913db4ba9815a31f8a28a196b7df96fe1cc46"

# =============================================================================
# Email settings
# =============================================================================
PRESET_EMAIL_SUBJECT = "Please sign this document"
PRESET_EMAIL_MESSAGE = "Hello, please review and sign this document."

# =============================================================================
# Bulk invite settings
# =============================================================================
PRESET_BULK_INVITE_SUBJECT = "Email subject for all signers from CSV"
PRESET_BULK_INVITE_MESSAGE = "Email message for all signers from CSV"
PRESET_BULK_DOCUMENT_NAME = "test_bulk_invite"
