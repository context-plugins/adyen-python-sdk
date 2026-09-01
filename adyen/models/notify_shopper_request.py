from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict


class NotifyShopperRequest(SdkBaseModel):
    amount: Amount
    """The amount of the upcoming payment."""

    billing_date: Optional[str] = Field(default=UNSET, alias="billingDate")
    """Date on which the subscription amount will be debited from the shopper. In YYYY-MM-DD format"""

    billing_sequence_number: Optional[str] = Field(default=UNSET, alias="billingSequenceNumber")
    """Sequence of the debit. Depends on Frequency and Billing Attempts Rule."""

    displayed_reference: Optional[str] = Field(default=UNSET, alias="displayedReference")
    """Reference of Pre-debit notification that is displayed to the shopper. Optional field. Maps to reference if
    missing"""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier with which you want to process the transaction."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    reference: str
    """Pre-debit notification reference sent by the merchant. This is a mandatory field"""

    shopper_reference: str = Field(alias="shopperReference")
    """The ID that uniquely identifies the shopper.

    This ``shopperReference`` must be the same as the ``shopperReference`` used in the initial payment."""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""


class NotifyShopperRequestDict(TypedDict):
    amount: Amount | AmountDict
    billing_date: NotRequired[str]
    billing_sequence_number: NotRequired[str]
    displayed_reference: NotRequired[str]
    merchant_account: str
    recurring_detail_reference: NotRequired[str]
    reference: str
    shopper_reference: str
    stored_payment_method_id: NotRequired[str]
