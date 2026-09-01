from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status16 import Status16OrStr


class UpdateNetworkTokenRequest(SdkBaseModel):
    status: Optional[Status16OrStr] = UNSET
    """The new status of the network token. Possible values: **active**, **suspended**, **closed**. The **closed**
    status is final and cannot be changed."""


class UpdateNetworkTokenRequestDict(TypedDict):
    status: NotRequired[Status16OrStr]
