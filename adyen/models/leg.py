from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class Leg(SdkBaseModel):
    carrier_code: Optional[str] = Field(default=UNSET, alias="carrierCode")
    """The `IATA <https://www.iata.org/services/pages/codes.aspx>`__ 2-letter accounting code (PAX) that identifies the
    carrier. This field is required if the airline data includes leg details.
    * Example: KLM = KL
    * minLength: 2 characters
    * maxLength: 2 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.leg[N].carrier_code``"""

    class_of_travel: Optional[str] = Field(default=UNSET, alias="classOfTravel")
    """A one-letter travel class identifier.
     The following are common:
     * F: first class
    * J: business class
    * Y: economy class
    * W: premium economy

    * Encoding: ASCII
    * minLength: 1 character
    * maxLength: 1 character
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.leg[N].class_of_travel``"""

    date_of_travel: Optional[RFC3339DateTime] = Field(default=UNSET, alias="dateOfTravel")
    """Date and time of travel in format ``yyyy-MM-ddTHH:mm``.
    * Use local time of departure airport.
    * minLength: 16 characters
    * maxLength: 16 characters
    * **additionalData key:** ``airline.leg[N].date_of_travel``"""

    departure_airport_code: Optional[str] = Field(default=UNSET, alias="departureAirportCode")
    """The `IATA <https://www.iata.org/services/pages/codes.aspx>`__ three-letter airport code of the departure airport.
    This field is required if the airline data includes leg details.

    * Encoding: ASCII
    * Example: Amsterdam = AMS
    * minLength: 3 characters
    * maxLength: 3 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.leg[N].depart_airport``"""

    departure_tax: Optional[int] = Field(default=UNSET, alias="departureTax")
    """The amount of `departure tax <https://en.wikipedia.org/wiki/Departure_tax>`__ charged, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Encoding: Numeric
    * minLength: 1
    * maxLength: 11
    * Must not be all zeros.
    * **additionalData key:** ``airline.leg[N].depart_tax``"""

    destination_airport_code: Optional[str] = Field(default=UNSET, alias="destinationAirportCode")
    """The `IATA <https://www.iata.org/services/pages/codes.aspx>`__ 3-letter airport code of the destination airport.
    This field is required if the airline data includes leg details.
    * Example: Amsterdam = AMS
    * Encoding: ASCII
    * minLength: 3 characters
    * maxLength: 3 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.leg[N].destination_code``"""

    fare_basis_code: Optional[str] = Field(default=UNSET, alias="fareBasisCode")
    """The `fare basis code <https://en.wikipedia.org/wiki/Fare_basis_code>`__, alphanumeric.
    * minLength: 1 character
    * maxLength: 15 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.leg[N].fare_base_code``"""

    flight_number: Optional[str] = Field(default=UNSET, alias="flightNumber")
    """The flight identifier.
    * minLength: 1 character
    * maxLength: 5 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.leg[N].flight_number``"""

    stop_over_code: Optional[str] = Field(default=UNSET, alias="stopOverCode")
    """A one-letter code that indicates whether the passenger is entitled to make a stopover. Can be a space, O if the
    passenger is entitled to make a stopover, or X if they are not.
    * Encoding: ASCII
    * minLength: 1 character
    * maxLength: 1 character
    * **additionalData key:** ``airline.leg[N].stop_over_code``"""


class LegDict(TypedDict):
    carrier_code: NotRequired[str]
    class_of_travel: NotRequired[str]
    date_of_travel: NotRequired[RFC3339DateTime]
    departure_airport_code: NotRequired[str]
    departure_tax: NotRequired[int]
    destination_airport_code: NotRequired[str]
    fare_basis_code: NotRequired[str]
    flight_number: NotRequired[str]
    stop_over_code: NotRequired[str]
