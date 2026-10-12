from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device import Device, DeviceDict
from .link1 import Link1, Link1Dict


class SearchRegisteredDevicesResponse(SdkBaseModel):
    data: Optional[list[Device]] = UNSET
    """Contains a list of registered SCA devices and their corresponding details."""

    items_total: Optional[int] = Field(default=UNSET, alias="itemsTotal")
    """The total amount of registered SCA devices that match the query parameters."""

    link: Optional[Link1] = UNSET
    """Contains links to the list pages."""

    pages_total: Optional[int] = Field(default=UNSET, alias="pagesTotal")
    """The total amount of list pages."""


class SearchRegisteredDevicesResponseDict(TypedDict):
    data: NotRequired[list[DeviceDict]]
    items_total: NotRequired[int]
    link: NotRequired[Link1Dict]
    pages_total: NotRequired[int]
