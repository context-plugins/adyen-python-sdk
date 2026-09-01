from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayU(SdkBaseModel):
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

    type_: Literal["payu_IN_upi"] = Field(default="payu_IN_upi", alias="type")
    """**payu_IN_upi**"""

    virtual_payment_address: Optional[str] = Field(default=UNSET, alias="virtualPaymentAddress")
    """The virtual payment address for UPI."""


class PayUDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    shopper_notification_reference: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: NotRequired[Literal["payu_IN_upi"]]
    virtual_payment_address: NotRequired[str]
