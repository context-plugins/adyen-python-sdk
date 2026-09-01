from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value6 import Value6OrStr


class WalletProviderDeviceType(SdkBaseModel):
    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[Value6OrStr]] = UNSET


class WalletProviderDeviceTypeDict(TypedDict):
    operation: str
    value: NotRequired[list[Value6OrStr]]
