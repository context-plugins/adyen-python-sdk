from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TwintInfo2(SdkBaseModel):
    """Details to provide if ``type`` is **twint**."""

    logo: str
    """Twint logo. Format: Base64-encoded string."""


class TwintInfo2Dict(TypedDict):
    logo: str
