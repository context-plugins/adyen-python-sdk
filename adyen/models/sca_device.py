from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.sca_device_type1 import ScaDeviceType1OrStr


class ScaDevice(SdkBaseModel):
    """A resource that contains information about a device, including its unique ID, name, and type."""

    id: str
    """The unique identifier of the SCA device you are registering."""

    name: str
    """The name of the SCA device that you are registering. You can use it to help your users identify the device."""

    type_: ScaDeviceType1OrStr = Field(alias="type")
    """Type of device registered.

    Possible values: **ios**, **android**, **browser**."""


class ScaDeviceDict(TypedDict):
    id: str
    name: str
    type_: ScaDeviceType1OrStr
