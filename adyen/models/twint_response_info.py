from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TwintResponseInfo(SdkBaseModel):
    logo: Optional[str] = UNSET
    """Twint logo. Format: Base64-encoded string."""


class TwintResponseInfoDict(TypedDict):
    logo: NotRequired[str]
