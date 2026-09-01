from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConnectedDevicesResponse(SdkBaseModel):
    unique_device_ids: Optional[list[str]] = Field(default=UNSET, alias="uniqueDeviceIds")
    """A list of the unique IDs of the devices that have an active cloud connection. The IDs are payment terminal IDs in
    the format _[terminal model]-[serial number]_ (for example, P400‑123456789), or SDK installation IDs as used in
    Mobile solutions."""


class ConnectedDevicesResponseDict(TypedDict):
    unique_device_ids: NotRequired[list[str]]
