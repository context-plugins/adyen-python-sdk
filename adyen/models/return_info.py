from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class ReturnInfo(SdkBaseModel):
    city: Optional[str] = UNSET
    """The city where the car must be returned.
    * Format: ASCII
    * maxLength: 18 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``carRental.returnCity``"""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The country where the car must be returned, in `ISO 3166-1 alpha-2
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format.
    * maxLength: 2 characters
    * **additionalData key:** ``carRental.returnCountry``"""

    date: Optional[Date] = UNSET
    """The date by which the car must be returned.
    * minLength: 10 characters
    * maxLength: 10 characters
    * Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: yyyy-MM-dd
    * **additionalData key:** ``carRental.returnDate``"""

    location_id: Optional[str] = Field(default=UNSET, alias="locationId")
    """The agency code, phone number, or address abbreviation.
    * Format: ASCII
    * maxLength: 10 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``carRental.returnLocationId``"""

    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    """The state or province where the car must be returned.
    * Format: ASCII
    * maxLength: 3 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``carRental.returnStateProvince``"""


class ReturnInfoDict(TypedDict):
    city: NotRequired[str]
    country_code: NotRequired[str]
    date: NotRequired[Date]
    location_id: NotRequired[str]
    state_or_province: NotRequired[str]
