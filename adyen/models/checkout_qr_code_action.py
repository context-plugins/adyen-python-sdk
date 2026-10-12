from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckoutQrCodeAction(SdkBaseModel):
    expires_at: Optional[str] = Field(default=UNSET, alias="expiresAt")
    """Expiry time of the QR code."""

    payment_data: Optional[str] = Field(default=UNSET, alias="paymentData")
    """Encoded payment data."""

    payment_method_type: Optional[str] = Field(default=UNSET, alias="paymentMethodType")
    """Specifies the payment method."""

    qr_code_data: Optional[str] = Field(default=UNSET, alias="qrCodeData")
    """The contents of the QR code as a UTF8 string."""

    type_: Literal["qrCode"] = Field(default="qrCode", alias="type")
    """**qrCode**"""

    url: Optional[str] = UNSET
    """Specifies the URL to redirect to."""


class CheckoutQrCodeActionDict(TypedDict):
    expires_at: NotRequired[str]
    payment_data: NotRequired[str]
    payment_method_type: NotRequired[str]
    qr_code_data: NotRequired[str]
    type_: Literal["qrCode"]
    url: NotRequired[str]
