from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StoredPaymentMethod3(SdkBaseModel):
    bank_account_number: Optional[str] = Field(default=UNSET, alias="bankAccountNumber")
    """The bank account number (without separators)."""

    bank_location_id: Optional[str] = Field(default=UNSET, alias="bankLocationId")
    """The location id of the bank. The field value is ``nil`` in most cases."""

    brand: Optional[str] = UNSET
    """The brand of the card."""

    cashtag: Optional[str] = UNSET
    """The shopper’s Cash App Pay Cashtag."""

    expiry_month: Optional[str] = Field(default=UNSET, alias="expiryMonth")
    """The two-digit month when the card expires"""

    expiry_year: Optional[str] = Field(default=UNSET, alias="expiryYear")
    """The last two digits of the year the card expires. For example, **22** for the year 2022."""

    external_token: Optional[str] = Field(default=UNSET, alias="externalToken")
    """The token issued by an external tokenization service representing the shopper's payment method"""

    holder_name: Optional[str] = Field(default=UNSET, alias="holderName")
    """The name of the payment method holder."""

    iban: Optional[str] = UNSET
    """The IBAN of the bank account."""

    id: Optional[str] = UNSET
    """A unique identifier of this stored payment method."""

    label: Optional[str] = UNSET
    """The shopper’s issuer account label"""

    last_four: Optional[str] = Field(default=UNSET, alias="lastFour")
    """The last four digits of the PAN."""

    name: Optional[str] = UNSET
    """The display name of the stored payment method."""

    network_tx_reference: Optional[str] = Field(default=UNSET, alias="networkTxReference")
    """Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions
    (MIT) framework from Mastercard or Visa.

    This contains either the Mastercard Trace ID or the Visa Transaction ID."""

    owner_name: Optional[str] = Field(default=UNSET, alias="ownerName")
    """The name of the bank account holder."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The shopper’s email address."""

    supported_recurring_processing_models: Optional[list[str]] = Field(
        default=UNSET, alias="supportedRecurringProcessingModels"
    )
    """The supported recurring processing models for this stored payment method."""

    supported_shopper_interactions: Optional[list[str]] = Field(default=UNSET, alias="supportedShopperInteractions")
    """The supported shopper interactions for this stored payment method."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of payment method."""


class StoredPaymentMethod3Dict(TypedDict):
    bank_account_number: NotRequired[str]
    bank_location_id: NotRequired[str]
    brand: NotRequired[str]
    cashtag: NotRequired[str]
    expiry_month: NotRequired[str]
    expiry_year: NotRequired[str]
    external_token: NotRequired[str]
    holder_name: NotRequired[str]
    iban: NotRequired[str]
    id: NotRequired[str]
    label: NotRequired[str]
    last_four: NotRequired[str]
    name: NotRequired[str]
    network_tx_reference: NotRequired[str]
    owner_name: NotRequired[str]
    shopper_email: NotRequired[str]
    supported_recurring_processing_models: NotRequired[list[str]]
    supported_shopper_interactions: NotRequired[list[str]]
    type_: NotRequired[str]
