from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Href6(SdkBaseModel):
    """The URL to where the user must be redirected after a payment has been canceled."""

    href: str
    """The full URL for the redirection."""


class Href6Dict(TypedDict):
    href: str
