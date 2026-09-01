from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdatePayoutSettingsRequest(SdkBaseModel):
    enabled: Optional[bool] = UNSET
    """Indicates if payouts to this bank account are enabled. Default: **true**.

    To receive payouts into this bank account, both ``enabled`` and ``allowed`` must be **true**."""


class UpdatePayoutSettingsRequestDict(TypedDict):
    enabled: NotRequired[bool]
