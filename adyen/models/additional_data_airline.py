from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataAirline(SdkBaseModel):
    airline_agency_invoice_number: Optional[str] = Field(default=UNSET, alias="airline.agency_invoice_number")
    """The reference number for the invoice, issued by the agency.
    * Encoding: ASCII
    * minLength: 1 character
    * maxLength: 6 characters"""

    airline_agency_plan_name: Optional[str] = Field(default=UNSET, alias="airline.agency_plan_name")
    """The two-letter agency plan identifier.
    * Encoding: ASCII
    * minLength: 2 characters
    * maxLength: 2 characters"""

    airline_airline_code: Optional[str] = Field(default=UNSET, alias="airline.airline_code")
    """The `IATA <https://www.iata.org/services/pages/codes.aspx>`__ 3-digit accounting code (PAX) that identifies the
    carrier.
    * Format: IATA 3-digit accounting code (PAX)
    * Example: KLM = 074
    * minLength: 3 characters
    * maxLength: 3 characters
    * Must not be all spaces
    * Must not be all zeros."""

    airline_airline_designator_code: Optional[str] = Field(default=UNSET, alias="airline.airline_designator_code")
    """The `IATA <https://www.iata.org/services/pages/codes.aspx>`__ 2-letter accounting code (PAX) that identifies the
    carrier.
    * Encoding: ASCII
    * Example: KLM = KL
    * minLength: 2 characters
    * maxLength: 2 characters
    * Must not be all spaces
    * Must not be all zeros."""

    airline_boarding_fee: Optional[str] = Field(default=UNSET, alias="airline.boarding_fee")
    """The amount charged for boarding the plane, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Encoding: Numeric
    * minLength: 1 character
    * maxLength: 18 characters"""

    airline_computerized_reservation_system: Optional[str] = Field(
        default=UNSET, alias="airline.computerized_reservation_system"
    )
    """The `CRS <https://en.wikipedia.org/wiki/Computer_reservation_system>`__ used to make the reservation and purchase
    the ticket.
    * Encoding: ASCII
    * minLength: 4 characters
    * maxLength: 4 characters"""

    airline_customer_reference_number: Optional[str] = Field(default=UNSET, alias="airline.customer_reference_number")
    """The alphanumeric customer reference number.
    * Encoding: ASCII
    * maxLength: 20 characters
    * If you send more than 20 characters, the customer reference number is truncated
    * Must not be all spaces"""

    airline_document_type: Optional[str] = Field(default=UNSET, alias="airline.document_type")
    """A code that identifies the type of item bought. The description of the code can appear on credit card statements.
    * Encoding: ASCII
    * Example: Passenger ticket = 01
    * minLength: 2 characters
    * maxLength: 2 characters"""

    airline_flight_date: Optional[str] = Field(default=UNSET, alias="airline.flight_date")
    """The flight departure date. Local time ``(HH:mm)`` is optional.
    * Date format: ``yyyy-MM-dd``
    * Date and time format: ``yyyy-MM-dd HH:mm``
    * minLength: 10 characters
    * maxLength: 16 characters"""

    airline_issue_date: Optional[str] = Field(default=UNSET, alias="airline.issue_date")
    """The date that the ticket was issued to the passenger.
    * minLength: 6 characters
    * maxLength: 6 characters
    * Date format: YYMMDD"""

    airline_leg_carrier_code: Optional[str] = Field(default=UNSET, alias="airline.leg.carrier_code")
    """The `IATA <https://www.iata.org/services/pages/codes.aspx>`__ 2-letter accounting code (PAX) that identifies the
    carrier. This field is required if the airline data includes leg details.
    * Example: KLM = KL
    * minLength: 2 characters
    * maxLength: 2 characters
    * Must not be all spaces
    * Must not be all zeros."""

    airline_leg_class_of_travel: Optional[str] = Field(default=UNSET, alias="airline.leg.class_of_travel")
    """A one-letter travel class identifier.
     The following are common:
     * F: first class
    * J: business class
    * Y: economy class
    * W: premium economy

    * Encoding: ASCII
    * minLength: 1 character
    * maxLength: 1 character
    * Must not be all spaces
    * Must not be all zeros."""

    airline_leg_date_of_travel: Optional[str] = Field(default=UNSET, alias="airline.leg.date_of_travel")
    """Date and time of travel in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ format ``yyyy-MM-dd HH:mm``.
    * Encoding: ASCII
    * minLength: 16 characters
    * maxLength: 16 characters"""

    airline_leg_depart_airport: Optional[str] = Field(default=UNSET, alias="airline.leg.depart_airport")
    """The `IATA <https://www.iata.org/services/pages/codes.aspx>`__ three-letter airport code of the departure airport.
    This field is required if the airline data includes leg details.

    * Encoding: ASCII
    * Example: Amsterdam = AMS
    * minLength: 3 characters
    * maxLength: 3 characters
    * Must not be all spaces
    * Must not be all zeros."""

    airline_leg_depart_tax: Optional[str] = Field(default=UNSET, alias="airline.leg.depart_tax")
    """The amount of `departure tax <https://en.wikipedia.org/wiki/Departure_tax>`__ charged, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * Encoding: Numeric
    * minLength: 1
    * maxLength: 12
    * Must not be all zeros."""

    airline_leg_destination_code: Optional[str] = Field(default=UNSET, alias="airline.leg.destination_code")
    """The `IATA <https://www.iata.org/services/pages/codes.aspx>`__ 3-letter airport code of the destination airport.
    This field is required if the airline data includes leg details.
    * Example: Amsterdam = AMS
    * Encoding: ASCII
    * minLength: 3 characters
    * maxLength: 3 characters
    * Must not be all spaces
    * Must not be all zeros."""

    airline_leg_fare_base_code: Optional[str] = Field(default=UNSET, alias="airline.leg.fare_base_code")
    """The `fare basis code <https://en.wikipedia.org/wiki/Fare_basis_code>`__, alphanumeric.
    * minLength: 1 character
    * maxLength: 15 characters
    * Must not be all spaces
    * Must not be all zeros."""

    airline_leg_flight_number: Optional[str] = Field(default=UNSET, alias="airline.leg.flight_number")
    """The flight identifier.
    * minLength: 1 character
    * maxLength: 5 characters
    * Must not be all spaces
    * Must not be all zeros."""

    airline_leg_stop_over_code: Optional[str] = Field(default=UNSET, alias="airline.leg.stop_over_code")
    """A one-letter code that indicates whether the passenger is entitled to make a stopover. Can be a space, O if the
    passenger is entitled to make a stopover, or X if they are not.
    * Encoding: ASCII
    * minLength: 1 character
    * maxLength: 1 character"""

    airline_passenger_date_of_birth: Optional[str] = Field(default=UNSET, alias="airline.passenger.date_of_birth")
    """The passenger's date of birth.

    Date format: ``yyyy-MM-dd``
    * minLength: 10
    * maxLength: 10"""

    airline_passenger_first_name: Optional[str] = Field(default=UNSET, alias="airline.passenger.first_name")
    """The passenger's first name.
    > This field is required if the airline data includes passenger details or leg details.
    * Encoding: ASCII"""

    airline_passenger_last_name: Optional[str] = Field(default=UNSET, alias="airline.passenger.last_name")
    """The passenger's last name.
    > This field is required if the airline data includes passenger details or leg details.
    * Encoding: ASCII"""

    airline_passenger_phone_number: Optional[str] = Field(default=UNSET, alias="airline.passenger.phone_number")
    """The passenger's phone number, including country code. This is an alphanumeric field that can include the '+' and
    '-' signs.
    * Encoding: ASCII
    * minLength: 3 characters
    * maxLength: 30 characters"""

    airline_passenger_traveller_type: Optional[str] = Field(default=UNSET, alias="airline.passenger.traveller_type")
    """The IATA passenger type code (PTC).
    * Encoding: ASCII
    * minLength: 3 characters
    * maxLength: 6 characters"""

    airline_passenger_name: str = Field(alias="airline.passenger_name")
    """The passenger's name, initials, and title.
    * Format: last name + first name or initials + title
    * Example: *FLYER / MARY MS*
    * minLength: 1 character
    * maxLength: 20 characters
    * If you send more than 20 characters, the name is truncated
    * Must not be all spaces
    * Must not be all zeros."""

    airline_ticket_issue_address: Optional[str] = Field(default=UNSET, alias="airline.ticket_issue_address")
    """The address of the organization that issued the ticket.
    * minLength: 0 characters
    * maxLength: 16 characters"""

    airline_ticket_number: Optional[str] = Field(default=UNSET, alias="airline.ticket_number")
    """The ticket's unique identifier.
    * minLength: 1 character
    * maxLength: 15 characters
    * Must not be all spaces
    * Must not be all zeros."""

    airline_travel_agency_code: Optional[str] = Field(default=UNSET, alias="airline.travel_agency_code")
    """The unique identifier from IATA or ARC for the travel agency that issues the ticket.
    * Encoding: ASCII
    * minLength: 1 character
    * maxLength: 8 characters
    * Must not be all spaces
    * Must not be all zeros."""

    airline_travel_agency_name: Optional[str] = Field(default=UNSET, alias="airline.travel_agency_name")
    """The name of the travel agency.

    * Encoding: ASCII
    * minLength: 1 character
    * maxLength: 25 characters
    * Must not be all spaces
    * Must not be all zeros."""


class AdditionalDataAirlineDict(TypedDict):
    airline_agency_invoice_number: NotRequired[str]
    airline_agency_plan_name: NotRequired[str]
    airline_airline_code: NotRequired[str]
    airline_airline_designator_code: NotRequired[str]
    airline_boarding_fee: NotRequired[str]
    airline_computerized_reservation_system: NotRequired[str]
    airline_customer_reference_number: NotRequired[str]
    airline_document_type: NotRequired[str]
    airline_flight_date: NotRequired[str]
    airline_issue_date: NotRequired[str]
    airline_leg_carrier_code: NotRequired[str]
    airline_leg_class_of_travel: NotRequired[str]
    airline_leg_date_of_travel: NotRequired[str]
    airline_leg_depart_airport: NotRequired[str]
    airline_leg_depart_tax: NotRequired[str]
    airline_leg_destination_code: NotRequired[str]
    airline_leg_fare_base_code: NotRequired[str]
    airline_leg_flight_number: NotRequired[str]
    airline_leg_stop_over_code: NotRequired[str]
    airline_passenger_date_of_birth: NotRequired[str]
    airline_passenger_first_name: NotRequired[str]
    airline_passenger_last_name: NotRequired[str]
    airline_passenger_phone_number: NotRequired[str]
    airline_passenger_traveller_type: NotRequired[str]
    airline_passenger_name: str
    airline_ticket_issue_address: NotRequired[str]
    airline_ticket_number: NotRequired[str]
    airline_travel_agency_code: NotRequired[str]
    airline_travel_agency_name: NotRequired[str]
