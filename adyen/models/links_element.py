from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinksElement(SdkBaseModel):
    """The link to the first page of the list., The link to the last page of the list., The link to the next page of the
    list., The link to the previous page of the list., The link to the list page you are currently viewing., Contains a
    link to the previous page., Contains a link to the next page."""

    href: Optional[str] = UNSET


class LinksElementDict(TypedDict):
    href: NotRequired[str]
