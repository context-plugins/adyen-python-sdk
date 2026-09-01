from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status71 import Status71OrStr


class CardOrderItemDeliveryStatus3(SdkBaseModel):
    """The status of the card delivery.

    Possible values: **created**, **rejected**, **processing**, **produced**, **shipped**, **delivered**,
    **notApplicable**, **unknown**."""

    error_message: Optional[str] = Field(default=UNSET, alias="errorMessage")
    """An error message."""

    status: Optional[Status71OrStr] = UNSET
    """The status of the PIN delivery."""

    tracking_number: Optional[str] = Field(default=UNSET, alias="trackingNumber")
    """The tracking number of the PIN delivery."""


class CardOrderItemDeliveryStatus3Dict(TypedDict):
    error_message: NotRequired[str]
    status: NotRequired[Status71OrStr]
    tracking_number: NotRequired[str]
