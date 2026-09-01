from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TravelAgency(SdkBaseModel):
    code: Optional[str] = UNSET
    """The unique identifier from IATA or ARC for the travel agency that issues the ticket.
    * Encoding: ASCII
    * minLength: 1 character
    * maxLength: 8 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.travel_agency_code``"""

    name: Optional[str] = UNSET
    """The name of the travel agency.

    * Encoding: ASCII
    * minLength: 1 character
    * maxLength: 25 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.travel_agency_name``"""


class TravelAgencyDict(TypedDict):
    code: NotRequired[str]
    name: NotRequired[str]
