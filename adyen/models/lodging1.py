from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Lodging1(SdkBaseModel):
    check_in_date: Optional[str] = Field(default=UNSET, alias="checkInDate")
    """The check-in date."""

    number_of_nights: Optional[int] = Field(default=UNSET, alias="numberOfNights")
    """The total number of nights the room is booked for."""


class Lodging1Dict(TypedDict):
    check_in_date: NotRequired[str]
    number_of_nights: NotRequired[int]
