from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_forward_response_from_url2 import CheckoutForwardResponseFromUrl2, CheckoutForwardResponseFromUrl2Dict


class CheckoutForwardResponse(SdkBaseModel):
    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """Merchant defined payment reference."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """Adyen's 16-character reference associated with the transaction/request. This value is globally unique. Use this
    reference when you communicate with us about this request."""

    response: CheckoutForwardResponseFromUrl2
    """The details of the response Adyen received from the third party."""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """The unique identifier of the token."""


class CheckoutForwardResponseDict(TypedDict):
    merchant_reference: NotRequired[str]
    psp_reference: NotRequired[str]
    response: CheckoutForwardResponseFromUrl2 | CheckoutForwardResponseFromUrl2Dict
    stored_payment_method_id: NotRequired[str]
