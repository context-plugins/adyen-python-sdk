from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payout_settings import PayoutSettings, PayoutSettingsDict


class PayoutSettingsResponse(SdkBaseModel):
    data: Optional[list[PayoutSettings]] = UNSET
    """The list of payout accounts."""


class PayoutSettingsResponseDict(TypedDict):
    data: NotRequired[list[PayoutSettings | PayoutSettingsDict]]
