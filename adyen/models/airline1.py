from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .agency import Agency, AgencyDict
from .leg import Leg, LegDict
from .passenger import Passenger, PassengerDict
from .ticket import Ticket, TicketDict
from .travel_agency import TravelAgency, TravelAgencyDict


class Airline1(SdkBaseModel):
    """`Airline enhanced scheme data <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/airline/>`__
    that may be required for processing the transaction and/or for interchange savings."""

    agency: Optional[Agency] = UNSET
    boarding_fee: Optional[int] = Field(default=UNSET, alias="boardingFee")
    """The amount charged for boarding the plane, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Encoding: Numeric
    * minLength: 1 character
    * maxLength: 11 characters
    * **additionalData key:** ``airline.boarding_fee``"""

    code: Optional[str] = UNSET
    """The `IATA <https://www.iata.org/services/pages/codes.aspx>`__ 3-digit accounting code (PAX) that identifies the
    carrier.
    * Format: IATA 3-digit accounting code (PAX)
    * Example: KLM = 074
    * minLength: 3 characters
    * maxLength: 3 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.airline_code``"""

    computerized_reservation_system: Optional[str] = Field(default=UNSET, alias="computerizedReservationSystem")
    """The `CRS <https://en.wikipedia.org/wiki/Computer_reservation_system>`__ used to make the reservation and purchase
    the ticket.
    * Encoding: ASCII
    * minLength: 4 characters
    * maxLength: 4 characters
    * **additionalData key:** ``airline.computerized_reservation_system``"""

    customer_reference_number: Optional[str] = Field(default=UNSET, alias="customerReferenceNumber")
    """The alphanumeric customer reference number.
    * Encoding: ASCII
    * maxLength: 20 characters
    * If you send more than 20 characters, the customer reference number is truncated
    * Must not start with a space or be all spaces.
    * **additionalData key:** ``airline.customer_reference_number``"""

    designator_code: Optional[str] = Field(default=UNSET, alias="designatorCode")
    """The `IATA <https://www.iata.org/services/pages/codes.aspx>`__ 2-letter accounting code (PAX) that identifies the
    carrier.
    * Encoding: ASCII
    * Example: KLM = KL
    * minLength: 2 characters
    * maxLength: 2 characters
    * Must not start with a space or be all spaces.
    * **additionalData key:** ``airline.airline_designator_code``"""

    document_type: Optional[str] = Field(default=UNSET, alias="documentType")
    """A code that identifies the type of item bought. The description of the code can appear on credit card statements.
    * Encoding: ASCII
    * Example: Passenger ticket = 01
    * minLength: 2 characters
    * maxLength: 2 characters
    * **additionalData key:** ``airline.document_type``"""

    flight_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="flightDate")
    """The flight departure date. Time is optional.
    * Format for date only: ``yyyy-MM-dd``
    * Format for date and time: ``yyyy-MM-ddTHH:mm``
    * Use local time of departure airport.
    * minLength: 10 characters
    * maxLength: 16 characters
    * **additionalData key:** ``airline.flight_date``"""

    legs: Optional[list[Leg]] = UNSET
    passenger_name: str = Field(alias="passengerName")
    """The passenger's name, initials, and title.
    * Format: last name + first name or initials + title
    * Example: *FLYER / MARY MS*
    * minLength: 1 character
    * maxLength: 20 characters
    * If you send more than 20 characters, the name is truncated
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.passenger_name``"""

    passengers: Optional[list[Passenger]] = UNSET
    ticket: Optional[Ticket] = UNSET
    travel_agency: Optional[TravelAgency] = Field(default=UNSET, alias="travelAgency")


class Airline1Dict(TypedDict):
    agency: NotRequired[AgencyDict]
    boarding_fee: NotRequired[int]
    code: NotRequired[str]
    computerized_reservation_system: NotRequired[str]
    customer_reference_number: NotRequired[str]
    designator_code: NotRequired[str]
    document_type: NotRequired[str]
    flight_date: NotRequired[RFC3339DateTime]
    legs: NotRequired[list[LegDict]]
    passenger_name: str
    passengers: NotRequired[list[PassengerDict]]
    ticket: NotRequired[TicketDict]
    travel_agency: NotRequired[TravelAgencyDict]
