from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sca_device import ScaDevice, ScaDeviceDict


class FinishScaDeviceRegistrationResponse(SdkBaseModel):
    sca_device: Optional[ScaDevice] = Field(default=UNSET, alias="scaDevice")
    """A resource that contains information about a device, including its unique ID, name, and type."""


class FinishScaDeviceRegistrationResponseDict(TypedDict):
    sca_device: NotRequired[ScaDevice | ScaDeviceDict]
