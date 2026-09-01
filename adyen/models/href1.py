from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Href1(SdkBaseModel):
    """The URL to where the user must be redirected after a successful payment."""

    href: str
    """The full URL for the redirection."""


class Href1Dict(TypedDict):
    href: str
