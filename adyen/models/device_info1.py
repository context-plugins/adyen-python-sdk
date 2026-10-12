from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .phone_info2 import PhoneInfo2, PhoneInfo2Dict


class DeviceInfo1(SdkBaseModel):
    """Contains information about the device used to provision the network token."""

    form_factor: Optional[str] = Field(default=UNSET, alias="formFactor")
    """The type of device used to provision the network token."""

    os_name: Optional[str] = Field(default=UNSET, alias="osName")
    """The operating system of the device used to provision the network token."""

    phone: Optional[PhoneInfo2] = UNSET
    """The information about the phone number of the device used to provision the the network token. This object is
    conditionally returned and is available for up to 24 hours after the provisioning request (access to this field
    requires a specific user role, please contact your Adyen representative to request permission)."""


class DeviceInfo1Dict(TypedDict):
    form_factor: NotRequired[str]
    os_name: NotRequired[str]
    phone: NotRequired[PhoneInfo2Dict]
