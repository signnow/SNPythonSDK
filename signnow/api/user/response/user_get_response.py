"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class UserGetResponse:
    """
    This class represents the response from the User GET API.
    """

    id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    active: Optional[str] = None
    verified: Optional[str] = None
    type: int = 0
    pro: int = 0
    created: Optional[str] = None
    primary_email: Optional[str] = None
    credits: int = 0
    has_atticus_access: bool = False
    is_logged_in: bool = False
    document_count: int = 0
    monthly_document_count: int = 0
    lifetime_document_count: int = 0
    googleapps: bool = False
    facebookapps: bool = False
    microsoftapps: bool = False
    registration_source: Optional[str] = None
    avatar_url: Optional[str] = None
    signer_phone_invite: Optional[str] = None
    locale: Optional[str] = None
    password_changed: Optional[int] = None
    upload_limit: Optional[int] = None

    # Complex nested objects - simplified for now
    emails: Optional[List[Dict[str, Any]]] = None
    subscriptions: Optional[List[Dict[str, Any]]] = None
    billing_period: Optional[Dict[str, Any]] = None
    premium_access: Optional[Dict[str, Any]] = None
    companies: Optional[List[Dict[str, Any]]] = None
    teams: Optional[List[Dict[str, Any]]] = None
    status: Optional[Dict[str, Any]] = None
    settings: Optional[Dict[str, Any]] = None
    organization_settings: Optional[List[Dict[str, Any]]] = None
    issue_notifications: Optional[List[Dict[str, Any]]] = None
    merchant_accounts: Optional[List[Dict[str, Any]]] = None
    cloud_export_account_details: Optional[Dict[str, Any]] = None
    organization: Optional[Dict[str, Any]] = None
