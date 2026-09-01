from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.value6 import Value6OrStr


class WalletProviderDeviceType2(SdkBaseModel):
    """Wallet Provider Device Type and the operation.

    Supported operations: **anyMatch**, **noneMatch**.

    Supported value inputs:
    - **MOBILE_PHONE**
    - **TABLET_OR_EREADER**
    - **WATCH_OR_WRISTBAND**
    - **WEARABLE**

    - **CARD**
    - **PC**
    - **OTHER**
    - **UNKNOWN**"""

    operation: str
    """Defines how the condition must be evaluated."""

    value: Optional[list[Value6OrStr]] = UNSET


class WalletProviderDeviceType2Dict(TypedDict):
    operation: str
    value: NotRequired[list[Value6OrStr]]
