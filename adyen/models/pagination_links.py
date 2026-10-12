from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links_element9 import LinksElement9, LinksElement9Dict
from .links_element10 import LinksElement10, LinksElement10Dict
from .links_element11 import LinksElement11, LinksElement11Dict
from .links_element12 import LinksElement12, LinksElement12Dict
from .links_element13 import LinksElement13, LinksElement13Dict


class PaginationLinks(SdkBaseModel):
    first: LinksElement9
    """The first page."""

    last: LinksElement10
    """The last page."""

    next: Optional[LinksElement11] = UNSET
    """The next page. Only present if there is a next page."""

    prev: Optional[LinksElement12] = UNSET
    """The previous page. Only present if there is a previous page."""

    self: LinksElement13
    """The current page."""


class PaginationLinksDict(TypedDict):
    first: LinksElement9Dict
    last: LinksElement10Dict
    next: NotRequired[LinksElement11Dict]
    prev: NotRequired[LinksElement12Dict]
    self: LinksElement13Dict
