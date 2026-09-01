from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataWallets(SdkBaseModel):
    androidpay_token: Optional[str] = Field(default=UNSET, alias="androidpay.token")
    """The Android Pay token retrieved from the SDK."""

    masterpass_transaction_id: Optional[str] = Field(default=UNSET, alias="masterpass.transactionId")
    """The Mastercard Masterpass Transaction ID retrieved from the SDK."""

    payment_token: Optional[str] = Field(default=UNSET, alias="payment.token")
    """The Apple Pay token retrieved from the SDK."""

    paywithgoogle_token: Optional[str] = Field(default=UNSET, alias="paywithgoogle.token")
    """The Google Pay token retrieved from the SDK."""

    samsungpay_token: Optional[str] = Field(default=UNSET, alias="samsungpay.token")
    """The Samsung Pay token retrieved from the SDK."""

    visacheckout_call_id: Optional[str] = Field(default=UNSET, alias="visacheckout.callId")
    """The Visa Checkout Call ID retrieved from the SDK."""


class AdditionalDataWalletsDict(TypedDict):
    androidpay_token: NotRequired[str]
    masterpass_transaction_id: NotRequired[str]
    payment_token: NotRequired[str]
    paywithgoogle_token: NotRequired[str]
    samsungpay_token: NotRequired[str]
    visacheckout_call_id: NotRequired[str]
