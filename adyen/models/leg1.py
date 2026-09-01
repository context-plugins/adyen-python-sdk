from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Leg1(SdkBaseModel):
    arrival_airport_code: Optional[str] = Field(default=UNSET, alias="arrivalAirportCode")
    """The IATA 3-letter airport code of the destination airport. This field is required if the airline data includes
    leg details."""

    basic_fare_code: Optional[str] = Field(default=UNSET, alias="basicFareCode")
    """The basic fare code for this leg."""

    carrier_code: Optional[str] = Field(default=UNSET, alias="carrierCode")
    """IATA code of the carrier operating the flight."""

    departure_airport_code: Optional[str] = Field(default=UNSET, alias="departureAirportCode")
    """The IATA three-letter airport code of the departure airport. This field is required if the airline data includes
    leg details"""

    departure_date: Optional[str] = Field(default=UNSET, alias="departureDate")
    """The flight departure date."""

    flight_number: Optional[str] = Field(default=UNSET, alias="flightNumber")
    """The flight identifier."""


class Leg1Dict(TypedDict):
    arrival_airport_code: NotRequired[str]
    basic_fare_code: NotRequired[str]
    carrier_code: NotRequired[str]
    departure_airport_code: NotRequired[str]
    departure_date: NotRequired[str]
    flight_number: NotRequired[str]
