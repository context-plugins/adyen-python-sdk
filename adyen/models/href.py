from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Href(SdkBaseModel):
    href: str
    """The full URL for the redirection."""


class HrefDict(TypedDict):
    href: str
