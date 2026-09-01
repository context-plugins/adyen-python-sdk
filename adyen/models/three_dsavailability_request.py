from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ThreeDsavailabilityRequest(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be required for a particular request.

    The ``additionalData`` object consists of entries, each of which includes the key and value."""

    brands: Optional[list[str]] = UNSET
    """List of brands."""

    card_number: Optional[str] = Field(default=UNSET, alias="cardNumber")
    """Card number or BIN."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """A recurring detail reference corresponding to a card."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """The shopper's reference to uniquely identify this shopper (e.g. user ID or account ID)."""


class ThreeDsavailabilityRequestDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    brands: NotRequired[list[str]]
    card_number: NotRequired[str]
    merchant_account: str
    recurring_detail_reference: NotRequired[str]
    shopper_reference: NotRequired[str]
