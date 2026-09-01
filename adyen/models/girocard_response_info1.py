from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_response_info1 import (
    TransactionDescriptionResponseInfo1,
    TransactionDescriptionResponseInfo1Dict,
)


class GirocardResponseInfo1(SdkBaseModel):
    """**girocard** details"""

    transaction_description: Optional[TransactionDescriptionResponseInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description."""


class GirocardResponseInfo1Dict(TypedDict):
    transaction_description: NotRequired[TransactionDescriptionResponseInfo1 | TransactionDescriptionResponseInfo1Dict]
