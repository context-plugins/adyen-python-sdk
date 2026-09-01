from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Agency(SdkBaseModel):
    invoice_number: Optional[str] = Field(default=UNSET, alias="invoiceNumber")
    """The reference number for the invoice, issued by the agency.
    * Encoding: ASCII
    * minLength: 1 character
    * maxLength: 6 characters
    * **additionalData key:** ``airline.agency_invoice_number``"""

    plan_name: Optional[str] = Field(default=UNSET, alias="planName")
    """The two-letter agency plan identifier.
    * Encoding: ASCII
    * minLength: 2 characters
    * maxLength: 2 characters
    * **additionalData key:** ``airline.agency_plan_name``"""


class AgencyDict(TypedDict):
    invoice_number: NotRequired[str]
    plan_name: NotRequired[str]
