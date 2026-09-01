from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.processing_type import ProcessingTypeOrStr
from .transaction_description_response_info1 import (
    TransactionDescriptionResponseInfo1,
    TransactionDescriptionResponseInfo1Dict,
)


class PulseResponseInfo(SdkBaseModel):
    processing_type: Optional[ProcessingTypeOrStr] = Field(default=UNSET, alias="processingType")
    """The type of transactions processed over this payment method.
     Allowed values:
    - **pos** for in-person payments.
    - **billpay** for subscription payments, both the initial payment and the later recurring payments. These
        transactions have ``recurringProcessingModel`` **Subscription**.
    - **ecom** for all other card not present transactions. This includes non-recurring transactions and transactions
        with ``recurringProcessingModel`` **CardOnFile** or **UnscheduledCardOnFile**."""

    transaction_description: Optional[TransactionDescriptionResponseInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description."""


class PulseResponseInfoDict(TypedDict):
    processing_type: NotRequired[ProcessingTypeOrStr]
    transaction_description: NotRequired[TransactionDescriptionResponseInfo1 | TransactionDescriptionResponseInfo1Dict]
