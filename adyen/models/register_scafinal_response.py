from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RegisterScafinalResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    """Specifies if the registration was initiated successfully."""


class RegisterScafinalResponseDict(TypedDict):
    success: NotRequired[bool]
