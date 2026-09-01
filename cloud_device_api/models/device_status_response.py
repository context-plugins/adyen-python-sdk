from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.device_status1 import DeviceStatus1OrStr


class DeviceStatusResponse(SdkBaseModel):
    device_id: Optional[str] = Field(default=UNSET, alias="deviceId")
    """The unique identification of the device. This can be a payment terminal ID in the format _[terminal
    model]-[serial number]_ (for example, P400‑123456789), or an SDK installation ID as used in Mobile solutions."""

    status: Optional[DeviceStatus1OrStr] = UNSET
    """Indicates if the device has an active cloud connection. Possible values:
    * **ONLINE**
    * **OFFLINE**"""


class DeviceStatusResponseDict(TypedDict):
    device_id: NotRequired[str]
    status: NotRequired[DeviceStatus1OrStr]
