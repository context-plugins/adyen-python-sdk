from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.subtype import SubtypeOrStr


class PayPal(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    order_id: Optional[str] = Field(default=UNSET, alias="orderID")
    """The unique ID associated with the order."""

    payee_preferred: Optional[str] = Field(default=UNSET, alias="payeePreferred")
    """IMMEDIATE_PAYMENT_REQUIRED or UNRESTRICTED"""

    payer_id: Optional[str] = Field(default=UNSET, alias="payerID")
    """The unique ID associated with the payer."""

    payer_selected: Optional[str] = Field(default=UNSET, alias="payerSelected")
    """PAYPAL or PAYPAL_CREDIT"""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    subtype: Optional[SubtypeOrStr] = UNSET
    """The type of flow to initiate."""

    type_: Literal["paypal"] = Field(default="paypal", alias="type")
    """**paypal**"""


class PayPalDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    order_id: NotRequired[str]
    payee_preferred: NotRequired[str]
    payer_id: NotRequired[str]
    payer_selected: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    subtype: NotRequired[SubtypeOrStr]
    type_: Literal["paypal"]
