from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sub_merchant_data21 import SubMerchantData21, SubMerchantData21Dict


class CertificateLoadingRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The unique identifier of your merchant account."""

    setup_token: str = Field(alias="setupToken")
    """The setup token provided by the SDK in a Mobile solution for in-person payments.
    - When using the Android SDK, obtain the token through the
        ``MerchantAuthenticationService.authenticate(setupToken)`` callback of ``AuthenticationService``.
    - When using the iOS SDK, obtain the token through the ``PaymentServiceDelegate.register(with:)`` callback of
        ``PaymentServiceDelegate``."""

    store: Optional[str] = UNSET
    """The reference of the store that you want to process transactions for. Do not include this parameter if your
    account structure uses merchant accounts as stores, or if you are a registered payment facilitator."""

    sub_merchant_data: Optional[SubMerchantData21] = Field(default=UNSET, alias="subMerchantData")
    """The details of the sub-merchant that you want to process transactions for.Required if you are a registered
    payment facilitator. Do not include this parameter if you are not a payment facilitator."""


class CertificateLoadingRequestDict(TypedDict):
    merchant_account: str
    setup_token: str
    store: NotRequired[str]
    sub_merchant_data: NotRequired[SubMerchantData21 | SubMerchantData21Dict]
