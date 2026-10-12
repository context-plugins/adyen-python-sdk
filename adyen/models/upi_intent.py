from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpiIntent(SdkBaseModel):
    app_id: Optional[str] = Field(default=UNSET, alias="appId")
    """TPAP (Third Party Application) Id that is being used to make the UPI payment"""

    billing_sequence_number: Optional[str] = Field(default=UNSET, alias="billingSequenceNumber")
    """The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The
    sequence number is included in the notification sent to the shopper."""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    shopper_notification_reference: Optional[str] = Field(default=UNSET, alias="shopperNotificationReference")
    """The ``shopperNotificationReference`` returned in the response when you requested to notify the shopper. Used for
    recurring payment only."""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    type_: Literal["upi_intent"] = Field(default="upi_intent", alias="type")
    """**upi_intent**"""


class UpiIntentDict(TypedDict):
    app_id: NotRequired[str]
    billing_sequence_number: NotRequired[str]
    checkout_attempt_id: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    shopper_notification_reference: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: Literal["upi_intent"]
