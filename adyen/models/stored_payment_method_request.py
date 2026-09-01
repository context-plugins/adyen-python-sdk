from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.recurring_processing_model1 import RecurringProcessingModel1OrStr
from .payment_method_to_store1 import PaymentMethodToStore1, PaymentMethodToStore1Dict


class StoredPaymentMethodRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    payment_method: PaymentMethodToStore1 = Field(alias="paymentMethod")
    """Contains the information required to store a payment method."""

    recurring_processing_model: RecurringProcessingModel1OrStr = Field(alias="recurringProcessingModel")
    """Defines a recurring payment type. Required when creating a token to store payment details. Allowed values:
    * ``Subscription`` – A transaction for a fixed or variable amount, which follows a fixed schedule.
    * ``CardOnFile`` – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel
        journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also
        considered a card-on-file transaction.
    * ``UnscheduledCardOnFile`` – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a
        non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance
        drops below a certain amount."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks."""

    shopper_ip: Optional[str] = Field(default=UNSET, alias="shopperIP")
    """The IP address of a shopper."""

    shopper_reference: str = Field(alias="shopperReference")
    """A unique identifier for the shopper (for example, user ID or account ID)."""


class StoredPaymentMethodRequestDict(TypedDict):
    merchant_account: str
    payment_method: PaymentMethodToStore1 | PaymentMethodToStore1Dict
    recurring_processing_model: RecurringProcessingModel1OrStr
    shopper_email: NotRequired[str]
    shopper_ip: NotRequired[str]
    shopper_reference: str
