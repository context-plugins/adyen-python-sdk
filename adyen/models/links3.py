from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links_element import LinksElement, LinksElementDict


class Links3(SdkBaseModel):
    next: Optional[LinksElement] = UNSET
    """Contains a link to the next page."""

    prev: Optional[LinksElement] = UNSET
    """Contains a link to the previous page."""


class Links3Dict(TypedDict):
    next: NotRequired[LinksElement | LinksElementDict]
    prev: NotRequired[LinksElement | LinksElementDict]
