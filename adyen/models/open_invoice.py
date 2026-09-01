from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type39 import Type39OrStr


class OpenInvoice(SdkBaseModel):
    billing_address: Optional[str] = Field(default=UNSET, alias="billingAddress")
    """The address where to send the invoice."""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    delivery_address: Optional[str] = Field(default=UNSET, alias="deliveryAddress")
    """The address where the goods should be delivered."""

    personal_details: Optional[str] = Field(default=UNSET, alias="personalDetails")
    """Shopper name, date of birth, phone number, and email address."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    type_: Optional[Type39OrStr] = Field(default=UNSET, alias="type")
    """**openinvoice**"""


class OpenInvoiceDict(TypedDict):
    billing_address: NotRequired[str]
    checkout_attempt_id: NotRequired[str]
    delivery_address: NotRequired[str]
    personal_details: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    type_: NotRequired[Type39OrStr]
