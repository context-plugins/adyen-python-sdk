from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StandalonePaymentCancelResponse(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    payment_reference: str = Field(alias="paymentReference")
    """The https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_reference of the payment
    to cancel."""

    psp_reference: str = Field(alias="pspReference")
    """Adyen's 16-character reference associated with the cancel request."""

    reference: Optional[str] = UNSET
    """Your reference for the cancel request."""

    status: Literal["received"] = "received"
    """The status of your request. This will always have the value **received**."""


class StandalonePaymentCancelResponseDict(TypedDict):
    merchant_account: str
    payment_reference: str
    psp_reference: str
    reference: NotRequired[str]
    status: NotRequired[Literal["received"]]
