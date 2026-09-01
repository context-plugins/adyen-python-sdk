from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShopperInteractionDevice(SdkBaseModel):
    """Shopper interaction device, such as terminal, mobile device or web browser, to initiate payment requests."""

    locale: Optional[str] = UNSET
    """Locale on the shopper interaction device."""

    os: Optional[str] = UNSET
    """Operating system running on the shopper interaction device."""

    os_version: Optional[str] = Field(default=UNSET, alias="osVersion")
    """Version of the operating system on the shopper interaction device."""


class ShopperInteractionDeviceDict(TypedDict):
    locale: NotRequired[str]
    os: NotRequired[str]
    os_version: NotRequired[str]
