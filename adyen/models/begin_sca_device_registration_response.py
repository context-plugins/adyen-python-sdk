from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sca_device import ScaDevice, ScaDeviceDict


class BeginScaDeviceRegistrationResponse(SdkBaseModel):
    sca_device: Optional[ScaDevice] = Field(default=UNSET, alias="scaDevice")
    """A resource that contains information about a device, including its unique ID, name, and type."""

    sdk_input: Optional[str] = Field(default=UNSET, alias="sdkInput")
    """A string that you must pass to the authentication SDK to continue with the registration process."""


class BeginScaDeviceRegistrationResponseDict(TypedDict):
    sca_device: NotRequired[ScaDevice | ScaDeviceDict]
    sdk_input: NotRequired[str]
