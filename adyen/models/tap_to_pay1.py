from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TapToPay1(SdkBaseModel):
    """Settings for Tap to Pay."""

    merchant_display_name: Optional[str] = Field(default=UNSET, alias="merchantDisplayName")
    """The text shown on the screen during the Tap to Pay transaction."""


class TapToPay1Dict(TypedDict):
    merchant_display_name: NotRequired[str]
