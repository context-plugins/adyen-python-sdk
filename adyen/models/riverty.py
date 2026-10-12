from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type49 import Type49, Type49OrStr


class Riverty(SdkBaseModel):
    billing_address: Optional[str] = Field(default=UNSET, alias="billingAddress")
    """The address where to send the invoice."""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    delivery_address: Optional[str] = Field(default=UNSET, alias="deliveryAddress")
    """The address where the goods should be delivered."""

    device_fingerprint: Optional[str] = Field(default=UNSET, alias="deviceFingerprint")
    """A string containing the shopper's device fingerprint. For more information, refer to `Device fingerprinting
    <https://docs.adyen.com/risk-management/device-fingerprinting>`__."""

    iban: Optional[str] = UNSET
    """The iban number of the customer"""

    merchant_data: Optional[str] = Field(default=UNSET, alias="merchantData")
    """Base64-encoded merchant metadata (Extra Merchant Data) forwarded to Riverty at authorization."""

    personal_details: Optional[str] = Field(default=UNSET, alias="personalDetails")
    """Shopper name, date of birth, phone number, and email address."""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    subtype: Optional[str] = UNSET
    """The payment method subtype."""

    type_: Type49OrStr = Field(default=Type49.RIVERTY, alias="type")
    """**riverty**"""


class RivertyDict(TypedDict):
    billing_address: NotRequired[str]
    checkout_attempt_id: NotRequired[str]
    delivery_address: NotRequired[str]
    device_fingerprint: NotRequired[str]
    iban: NotRequired[str]
    merchant_data: NotRequired[str]
    personal_details: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    subtype: NotRequired[str]
    type_: Type49OrStr
