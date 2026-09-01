from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Logo(SdkBaseModel):
    data: Optional[str] = UNSET
    """The image file, converted to a Base64-encoded string, of the logo to be shown on the terminal."""


class LogoDict(TypedDict):
    data: NotRequired[str]
