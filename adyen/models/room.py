from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Room(SdkBaseModel):
    number_of_nights: Optional[int] = Field(default=UNSET, alias="numberOfNights")
    """The total number of nights the room is booked for.
    * Format: Numeric
    * Must be a number between 1 and 99
    * **additionalData key:** ``lodging.room[N].numberOfNights``"""

    rate: Optional[int] = UNSET
    """Room rate per night, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``lodging.room[N].rate``"""


class RoomDict(TypedDict):
    number_of_nights: NotRequired[int]
    rate: NotRequired[int]
