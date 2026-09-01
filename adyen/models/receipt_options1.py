from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReceiptOptions1(SdkBaseModel):
    """Generic receipt settings."""

    header_line1: Optional[str] = Field(default=UNSET, alias="headerLine1")
    """The text of the first header line to be shown on the receipt."""

    header_line2: Optional[str] = Field(default=UNSET, alias="headerLine2")
    """The text of the second header line to be shown on the receipt."""

    logo: Optional[str] = UNSET
    """The receipt logo converted to a Base64-encoded string. The image must be a .bmp file of < 256 KB, dimensions 240
    (H) x 384 (W) px."""

    prompt_before_printing: Optional[bool] = Field(default=UNSET, alias="promptBeforePrinting")
    """Indicates whether a screen appears asking if you want to print the shopper receipt."""

    qr_code_data: Optional[str] = Field(default=UNSET, alias="qrCodeData")
    """Data to print on the receipt as a QR code. This can include static text and the following variables:

    - ``${merchantreference}``: the merchant reference of the transaction.
    - ``${pspreference}``: the PSP reference of the transaction.

     For example, **http://www.example.com/order/${pspreference}/${merchantreference}**."""


class ReceiptOptions1Dict(TypedDict):
    header_line1: NotRequired[str]
    header_line2: NotRequired[str]
    logo: NotRequired[str]
    prompt_before_printing: NotRequired[bool]
    qr_code_data: NotRequired[str]
