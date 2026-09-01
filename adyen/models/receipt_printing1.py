from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReceiptPrinting1(SdkBaseModel):
    """Transaction outcomes that you want the terminal to print a merchant receipt or a shopper receipt for."""

    merchant_approved: Optional[bool] = Field(default=UNSET, alias="merchantApproved")
    """Print a merchant receipt when the payment is approved."""

    merchant_cancelled: Optional[bool] = Field(default=UNSET, alias="merchantCancelled")
    """Print a merchant receipt when the transaction is cancelled."""

    merchant_capture_approved: Optional[bool] = Field(default=UNSET, alias="merchantCaptureApproved")
    """Print a merchant receipt when capturing the payment is approved."""

    merchant_capture_refused: Optional[bool] = Field(default=UNSET, alias="merchantCaptureRefused")
    """Print a merchant receipt when capturing the payment is refused."""

    merchant_refund_approved: Optional[bool] = Field(default=UNSET, alias="merchantRefundApproved")
    """Print a merchant receipt when the refund is approved."""

    merchant_refund_refused: Optional[bool] = Field(default=UNSET, alias="merchantRefundRefused")
    """Print a merchant receipt when the refund is refused."""

    merchant_refused: Optional[bool] = Field(default=UNSET, alias="merchantRefused")
    """Print a merchant receipt when the payment is refused."""

    merchant_void: Optional[bool] = Field(default=UNSET, alias="merchantVoid")
    """Print a merchant receipt when a previous transaction is voided."""

    shopper_approved: Optional[bool] = Field(default=UNSET, alias="shopperApproved")
    """Print a shopper receipt when the payment is approved."""

    shopper_cancelled: Optional[bool] = Field(default=UNSET, alias="shopperCancelled")
    """Print a shopper receipt when the transaction is cancelled."""

    shopper_capture_approved: Optional[bool] = Field(default=UNSET, alias="shopperCaptureApproved")
    """Print a shopper receipt when capturing the payment is approved."""

    shopper_capture_refused: Optional[bool] = Field(default=UNSET, alias="shopperCaptureRefused")
    """Print a shopper receipt when capturing the payment is refused."""

    shopper_refund_approved: Optional[bool] = Field(default=UNSET, alias="shopperRefundApproved")
    """Print a shopper receipt when the refund is approved."""

    shopper_refund_refused: Optional[bool] = Field(default=UNSET, alias="shopperRefundRefused")
    """Print a shopper receipt when the refund is refused."""

    shopper_refused: Optional[bool] = Field(default=UNSET, alias="shopperRefused")
    """Print a shopper receipt when the payment is refused."""

    shopper_void: Optional[bool] = Field(default=UNSET, alias="shopperVoid")
    """Print a shopper receipt when a previous transaction is voided."""


class ReceiptPrinting1Dict(TypedDict):
    merchant_approved: NotRequired[bool]
    merchant_cancelled: NotRequired[bool]
    merchant_capture_approved: NotRequired[bool]
    merchant_capture_refused: NotRequired[bool]
    merchant_refund_approved: NotRequired[bool]
    merchant_refund_refused: NotRequired[bool]
    merchant_refused: NotRequired[bool]
    merchant_void: NotRequired[bool]
    shopper_approved: NotRequired[bool]
    shopper_cancelled: NotRequired[bool]
    shopper_capture_approved: NotRequired[bool]
    shopper_capture_refused: NotRequired[bool]
    shopper_refund_approved: NotRequired[bool]
    shopper_refund_refused: NotRequired[bool]
    shopper_refused: NotRequired[bool]
    shopper_void: NotRequired[bool]
