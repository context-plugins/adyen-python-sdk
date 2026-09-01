from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment_account_status2 import PaymentAccountStatus2, PaymentAccountStatus2Dict
from .payment_receipt import PaymentReceipt, PaymentReceiptDict
from .response11 import Response11, Response11Dict


class BalanceInquiryResponse(SdkBaseModel):
    """Content of the Balance Inquiry Response message. It conveys the balance and the identification of the associated
    payment, loyalty or stored value account."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    payment_account_status: Optional[PaymentAccountStatus2] = Field(default=UNSET, alias="PaymentAccountStatus")
    """Data related to the result of a Balance Inquiry request. If BalanceInquiryRequest. PaymentAccount present."""

    payment_receipt: Optional[list[PaymentReceipt]] = Field(default=UNSET, alias="PaymentReceipt")


class BalanceInquiryResponseDict(TypedDict):
    response: Response11 | Response11Dict
    payment_account_status: NotRequired[PaymentAccountStatus2 | PaymentAccountStatus2Dict]
    payment_receipt: NotRequired[list[PaymentReceipt | PaymentReceiptDict]]
