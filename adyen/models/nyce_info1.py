from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.processing_type import ProcessingTypeOrStr
from .transaction_description_info1 import TransactionDescriptionInfo1, TransactionDescriptionInfo1Dict


class NyceInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **nyce**."""

    processing_type: ProcessingTypeOrStr = Field(alias="processingType")
    """The type of transactions processed over this payment method.
     Allowed values:
    - **pos** for in-person payments.
    - **billpay** for subscription payments, both the initial payment and the later recurring payments. These
        transactions have ``recurringProcessingModel`` **Subscription**.
    - **ecom** for all other card not present transactions. This includes non-recurring transactions and transactions
        with ``recurringProcessingModel`` **CardOnFile** or **UnscheduledCardOnFile**."""

    transaction_description: Optional[TransactionDescriptionInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""


class NyceInfo1Dict(TypedDict):
    processing_type: ProcessingTypeOrStr
    transaction_description: NotRequired[TransactionDescriptionInfo1 | TransactionDescriptionInfo1Dict]
