from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .card import Card, CardDict
from .name import Name, NameDict


class FundSource11(SdkBaseModel):
    """The person or entity funding the money."""

    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """A map of name-value pairs for passing additional or industry-specific data."""

    billing_address: Optional[Address] = Field(default=UNSET, alias="billingAddress")
    """The address where to send the invoice."""

    card: Optional[Card] = UNSET
    """Credit card data.

    Optional if ``shopperReference`` and ``selectedRecurringDetailReference`` are provided."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """Email address of the person."""

    shopper_name: Optional[Name] = Field(default=UNSET, alias="shopperName")
    """Name of the person."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """Phone number of the person"""


class FundSource11Dict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    billing_address: NotRequired[AddressDict]
    card: NotRequired[CardDict]
    shopper_email: NotRequired[str]
    shopper_name: NotRequired[NameDict]
    telephone_number: NotRequired[str]
