from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CashAppUpdateInfo(SdkBaseModel):
    logo_url: Optional[str] = Field(default=UNSET, alias="logoUrl")
    """The URL of the logo image shown in Cash App checkout next to payments."""

    merchant_name: Optional[str] = Field(default=UNSET, alias="merchantName")
    """The merchant display name shown in Cash App checkout."""


class CashAppUpdateInfoDict(TypedDict):
    logo_url: NotRequired[str]
    merchant_name: NotRequired[str]
