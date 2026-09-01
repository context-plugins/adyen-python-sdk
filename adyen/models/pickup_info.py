from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class PickupInfo(SdkBaseModel):
    city: Optional[str] = UNSET
    """The city where the car is rented.
    * Format: ASCII
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``carRental.locationCity``"""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The country where the car is rented, in `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
    format.
    * maxLength: 2 characters
    * **additionalData key:** ``carRental.locationCountry``"""

    date: Optional[Date] = UNSET
    """The pick-up date.
    * minLength: 10 characters
    * maxLength: 10 characters
    * Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: yyyy-MM-dd
    * **additionalData key:** ``carRental.checkOutDate``"""

    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    """The state or province where the car is rented.
    * maxLength: 3 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``carRental.locationStateProvince``"""


class PickupInfoDict(TypedDict):
    city: NotRequired[str]
    country_code: NotRequired[str]
    date: NotRequired[Date]
    state_or_province: NotRequired[str]
