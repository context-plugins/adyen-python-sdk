from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount26 import Amount26, Amount26Dict
from .enums.result_code2 import ResultCode2OrStr
from .payment_response3 import PaymentResponse3, PaymentResponse3Dict


class Payment(SdkBaseModel):
    amount: Optional[Amount26] = UNSET
    """Authorised amount in the transaction."""

    payment_method: Optional[PaymentResponse3] = Field(default=UNSET, alias="paymentMethod")
    """Only returned for ``resultCode``: **Authorised**. Details about the payment method used in the transaction."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """Adyen's 16-character reference associated with the transaction/request. This value is globally unique. Use this
    reference when you communicate with us about this request."""

    result_code: Optional[ResultCode2OrStr] = Field(default=UNSET, alias="resultCode")
    """The result of the payment. For more information, see `Result codes
    <https://docs.adyen.com/online-payments/payment-result-codes>`__.

    Possible values:

    * **Authorised** – The payment was successfully authorised. This state serves as an indicator to proceed with the
        delivery of goods and services. This is a final state.
    * **Received** – Indicates the payment request was successfully received by Adyen, and will be processed. This is
        the initial state for all payments.
    * **Pending** – The payment order was successfully received but the final status of the payment is not available
        yet. This is common for payment methods with an asynchronous flow."""


class PaymentDict(TypedDict):
    amount: NotRequired[Amount26Dict]
    payment_method: NotRequired[PaymentResponse3Dict]
    psp_reference: NotRequired[str]
    result_code: NotRequired[ResultCode2OrStr]
