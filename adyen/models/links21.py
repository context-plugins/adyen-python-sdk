from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links_element import LinksElement, LinksElementDict


class Links21(SdkBaseModel):
    """Contains links to the next and previous page whenever applicable."""

    next: Optional[LinksElement] = UNSET
    """Contains a link to the next page."""

    prev: Optional[LinksElement] = UNSET
    """Contains a link to the previous page."""


class Links21Dict(TypedDict):
    next: NotRequired[LinksElementDict]
    prev: NotRequired[LinksElementDict]
