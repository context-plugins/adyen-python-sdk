from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class Passenger(SdkBaseModel):
    date_of_birth: Optional[Date] = Field(default=UNSET, alias="dateOfBirth")
    """The passenger's date of birth.
    * Format ``yyyy-MM-dd``
    * minLength: 10
    * maxLength: 10
    * **additionalData key:** ``airline.passenger[N].date_of_birth``"""

    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    """The passenger's first name.
    > This field is required if the airline data includes passenger details or leg details.
    * Encoding: ASCII
    * **additionalData key:** ``airline.passenger[N].first_name``"""

    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    """The passenger's last name.
    > This field is required if the airline data includes passenger details or leg details.
    * Encoding: ASCII
    * **additionalData key:** ``airline.passenger[N].last_name``"""

    phone_number: Optional[str] = Field(default=UNSET, alias="phoneNumber")
    """The passenger's phone number, including country code. This is an alphanumeric field that can include the '+' and
    '-' signs.
    * Encoding: ASCII
    * minLength: 3 characters
    * maxLength: 30 characters
    * **additionalData key:** ``airline.passenger[N].phone_number``"""

    traveller_type: Optional[str] = Field(default=UNSET, alias="travellerType")
    """The IATA passenger type code (PTC).
    * Encoding: ASCII
    * minLength: 3 characters
    * maxLength: 6 characters
    * **additionalData key:** ``airline.passenger[N].traveller_type``"""


class PassengerDict(TypedDict):
    date_of_birth: NotRequired[Date]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    phone_number: NotRequired[str]
    traveller_type: NotRequired[str]
