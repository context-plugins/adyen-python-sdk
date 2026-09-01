from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Href3(SdkBaseModel):
    """A short-lived URL that redirects the user to the iDEAL profile management page."""

    href: str
    """The full URL for the redirection."""


class Href3Dict(TypedDict):
    href: str
