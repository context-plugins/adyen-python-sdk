from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .payment_instrument1 import PaymentInstrument1, PaymentInstrument1Dict


class PaginatedPaymentInstrumentsResponse(SdkBaseModel):
    has_next: bool = Field(alias="hasNext")
    """Indicates whether there are more items on the next page."""

    has_previous: bool = Field(alias="hasPrevious")
    """Indicates whether there are more items on the previous page."""

    payment_instruments: list[PaymentInstrument1] = Field(alias="paymentInstruments")
    """List of payment instruments associated with the balance account."""


class PaginatedPaymentInstrumentsResponseDict(TypedDict):
    has_next: bool
    has_previous: bool
    payment_instruments: list[PaymentInstrument1Dict]
