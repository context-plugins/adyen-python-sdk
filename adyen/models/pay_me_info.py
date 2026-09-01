from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PayMeInfo(SdkBaseModel):
    display_name: str = Field(alias="displayName")
    """Merchant display name"""

    logo: str
    """Merchant logo. Format: Base64-encoded string."""

    support_email: str = Field(alias="supportEmail")
    """The email address of merchant support."""


class PayMeInfoDict(TypedDict):
    display_name: str
    logo: str
    support_email: str
