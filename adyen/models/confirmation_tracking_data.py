from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status15 import Status15OrStr


class ConfirmationTrackingData(SdkBaseModel):
    status: Status15OrStr
    """The status of the transfer.

    Possible values:

     - **credited**: the funds are credited to your user's transfer instrument or bank account.- **accepted**: the
            request is accepted by the integration."""

    type_: Literal["confirmation"] = Field(default="confirmation", alias="type")
    """The type of the tracking event.

    Possible values:

     - **confirmation**: the transfer passed Adyen's internal review."""


class ConfirmationTrackingDataDict(TypedDict):
    status: Status15OrStr
    type_: Literal["confirmation"]
