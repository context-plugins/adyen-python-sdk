from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class Ticket(SdkBaseModel):
    issue_address: Optional[str] = Field(default=UNSET, alias="issueAddress")
    """The address of the organization that issued the ticket.
    * minLength: 0 characters
    * maxLength: 16 characters
    * **additionalData key:** ``airline.ticket_issue_address``"""

    issue_date: Optional[Date] = Field(default=UNSET, alias="issueDate")
    """The date that the ticket was issued to the passenger.
    * minLength: 10 characters
    * maxLength: 10 characters
    * Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: yyyy-MM-dd
    * **additionalData key:** ``airline.issue_date``"""

    number: Optional[str] = UNSET
    """The ticket's unique identifier.
    * minLength: 1 character
    * maxLength: 15 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``airline.ticket_number``"""


class TicketDict(TypedDict):
    issue_address: NotRequired[str]
    issue_date: NotRequired[Date]
    number: NotRequired[str]
