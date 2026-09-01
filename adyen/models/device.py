from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type101 import Type101OrStr


class Device(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique identifier of the SCA device."""

    name: Optional[str] = UNSET
    """The name of the SCA device. You can show this name to your user to help them identify the device."""

    payment_instrument_id: Optional[str] = Field(default=UNSET, alias="paymentInstrumentId")
    """The unique identifier of the payment instrument that is associated with the SCA device."""

    type_: Optional[Type101OrStr] = Field(default=UNSET, alias="type")
    """The type of device.

    Possible values: **ios**, **android**, **browser**."""


class DeviceDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    payment_instrument_id: NotRequired[str]
    type_: NotRequired[Type101OrStr]
