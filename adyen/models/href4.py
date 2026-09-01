from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Href4(SdkBaseModel):
    """A short-lived URL that redirects the user to the iDEAL page that is required for authentication."""

    href: str
    """The full URL for the redirection."""


class Href4Dict(TypedDict):
    href: str
