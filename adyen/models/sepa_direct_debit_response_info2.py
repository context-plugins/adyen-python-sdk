from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_response_info1 import (
    TransactionDescriptionResponseInfo1,
    TransactionDescriptionResponseInfo1Dict,
)


class SepaDirectDebitResponseInfo2(SdkBaseModel):
    """**sepadirectdebit** details"""

    creditor_id: Optional[str] = Field(default=UNSET, alias="creditorId")
    """Creditor id"""

    transaction_description: Optional[TransactionDescriptionResponseInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description."""


class SepaDirectDebitResponseInfo2Dict(TypedDict):
    creditor_id: NotRequired[str]
    transaction_description: NotRequired[TransactionDescriptionResponseInfo1 | TransactionDescriptionResponseInfo1Dict]
