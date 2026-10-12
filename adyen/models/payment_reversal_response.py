from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentReversalResponse(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    payment_psp_reference: str = Field(alias="paymentPspReference")
    """The https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the payment
    to reverse."""

    psp_reference: str = Field(alias="pspReference")
    """Adyen's 16-character reference associated with the reversal request."""

    reference: Optional[str] = UNSET
    """Your reference for the reversal request."""

    status: Literal["received"] = "received"
    """The status of your request. This will always have the value **received**."""


class PaymentReversalResponseDict(TypedDict):
    merchant_account: str
    payment_psp_reference: str
    psp_reference: str
    reference: NotRequired[str]
    status: Literal["received"]
