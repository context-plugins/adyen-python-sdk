from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MerchantDevice(SdkBaseModel):
    """Merchant device information."""

    os: Optional[str] = UNSET
    """Operating system running on the merchant device."""

    os_version: Optional[str] = Field(default=UNSET, alias="osVersion")
    """Version of the operating system on the merchant device."""

    reference: Optional[str] = UNSET
    """Merchant device reference."""


class MerchantDeviceDict(TypedDict):
    os: NotRequired[str]
    os_version: NotRequired[str]
    reference: NotRequired[str]
