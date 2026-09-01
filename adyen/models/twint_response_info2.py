from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TwintResponseInfo2(SdkBaseModel):
    """**twint** details"""

    logo: Optional[str] = UNSET
    """Twint logo. Format: Base64-encoded string."""


class TwintResponseInfo2Dict(TypedDict):
    logo: NotRequired[str]
