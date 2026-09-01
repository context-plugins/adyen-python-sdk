from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status61 import Status61OrStr


class CardOrder(SdkBaseModel):
    begin_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="beginDate")
    """The date when the card order is created."""

    card_manufacturing_profile_id: Optional[str] = Field(default=UNSET, alias="cardManufacturingProfileId")
    """The unique identifier of the card manufacturer profile."""

    closed_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="closedDate")
    """The date when the card order processing ends."""

    end_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="endDate")
    """The date when you manually closed the card order.

    Card orders are automatically closed by the end of the day it was created. If you manually closed it beforehand, the
    closing date is shown as the ``endDate``."""

    id: Optional[str] = UNSET
    """The unique identifier of the card order."""

    lock_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="lockDate")
    """The date when the card order processing begins."""

    service_center: Optional[str] = Field(default=UNSET, alias="serviceCenter")
    """The service center."""

    status: Optional[Status61OrStr] = UNSET
    """The status of the card order.

    Possible values: **Open**, **Closed**."""


class CardOrderDict(TypedDict):
    begin_date: NotRequired[RFC3339DateTime]
    card_manufacturing_profile_id: NotRequired[str]
    closed_date: NotRequired[RFC3339DateTime]
    end_date: NotRequired[RFC3339DateTime]
    id: NotRequired[str]
    lock_date: NotRequired[RFC3339DateTime]
    service_center: NotRequired[str]
    status: NotRequired[Status61OrStr]
