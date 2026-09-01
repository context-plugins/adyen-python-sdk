from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayMeResponseInfo1(SdkBaseModel):
    """**payme** details"""

    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """Merchant display name"""

    logo: Optional[str] = UNSET
    """Merchant logo. Format: Base64-encoded string."""

    support_email: Optional[str] = Field(default=UNSET, alias="supportEmail")
    """The email address of merchant support."""


class PayMeResponseInfo1Dict(TypedDict):
    display_name: NotRequired[str]
    logo: NotRequired[str]
    support_email: NotRequired[str]
