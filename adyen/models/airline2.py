from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .leg1 import Leg1, Leg1Dict


class Airline2(SdkBaseModel):
    legs: Optional[list[Leg1]] = UNSET
    """Details about the flight legs for this ticket."""

    ticket_number: Optional[str] = Field(default=UNSET, alias="ticketNumber")
    """The ticket's unique identifier"""


class Airline2Dict(TypedDict):
    legs: NotRequired[list[Leg1Dict]]
    ticket_number: NotRequired[str]
