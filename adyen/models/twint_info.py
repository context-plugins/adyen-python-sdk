from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TwintInfo(SdkBaseModel):
    logo: str
    """Twint logo. Format: Base64-encoded string."""


class TwintInfoDict(TypedDict):
    logo: str
