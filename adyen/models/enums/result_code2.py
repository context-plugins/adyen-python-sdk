from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ResultCode2(str, Enum):
    """The result of the payment. For more information, see `Result codes
    <https://docs.adyen.com/online-payments/payment-result-codes>`__.

    Possible values:

    * **Authorised** – The payment was successfully authorised. This state serves as an indicator to proceed with the
        delivery of goods and services. This is a final state.
    * **Received** – Indicates the payment request was successfully received by Adyen, and will be processed. This is
        the initial state for all payments.
    * **Pending** – The payment order was successfully received but the final status of the payment is not available
        yet. This is common for payment methods with an asynchronous flow."""

    AUTHORISED = "Authorised"
    RECEIVED = "Received"
    PENDING = "Pending"

    __str__ = str.__str__


ResultCode2OrStr: TypeAlias = Annotated[ResultCode2 | str, open_enum_validator(ResultCode2)]
