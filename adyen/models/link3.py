from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links_element import LinksElement, LinksElementDict


class Link3(SdkBaseModel):
    """A list of hyperlinks to resources related to this response."""

    first: Optional[LinksElement] = UNSET
    """The link to the first page of the list."""

    last: Optional[LinksElement] = UNSET
    """The link to the last page of the list."""

    next: Optional[LinksElement] = UNSET
    """The link to the next page of the list."""

    previous: Optional[LinksElement] = UNSET
    """The link to the previous page of the list."""

    self: Optional[LinksElement] = UNSET
    """The link to the list page you are currently viewing."""


class Link3Dict(TypedDict):
    first: NotRequired[LinksElementDict]
    last: NotRequired[LinksElementDict]
    next: NotRequired[LinksElementDict]
    previous: NotRequired[LinksElementDict]
    self: NotRequired[LinksElementDict]
