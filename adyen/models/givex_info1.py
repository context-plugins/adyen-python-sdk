from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.payment_flow import PaymentFlowOrStr


class GivexInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **givex**."""

    currency_code: str = Field(alias="currencyCode")
    """The three-character ISO currency code, such as **EUR**."""

    password: str
    """The password provided by the acquirer."""

    payment_flow: PaymentFlowOrStr = Field(alias="paymentFlow")
    """The sales channel used for the payment."""

    username: str
    """The username provided by the acquirer."""


class GivexInfo1Dict(TypedDict):
    currency_code: str
    password: str
    payment_flow: PaymentFlowOrStr
    username: str
