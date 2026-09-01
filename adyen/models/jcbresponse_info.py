from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_response_info1 import (
    TransactionDescriptionResponseInfo1,
    TransactionDescriptionResponseInfo1Dict,
)


class JcbresponseInfo(SdkBaseModel):
    mid_number: Optional[str] = Field(default=UNSET, alias="midNumber")
    """MID (Merchant ID) number."""

    reuse_mid_number: Optional[bool] = Field(default=UNSET, alias="reuseMidNumber")
    """Indicates whether the JCB Merchant ID is reused from a previously setup JCB payment method."""

    service_level: Optional[str] = Field(default=UNSET, alias="serviceLevel")
    """Specifies the service level (settlement type) of this payment method."""

    transaction_description: Optional[TransactionDescriptionResponseInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description."""


class JcbresponseInfoDict(TypedDict):
    mid_number: NotRequired[str]
    reuse_mid_number: NotRequired[bool]
    service_level: NotRequired[str]
    transaction_description: NotRequired[TransactionDescriptionResponseInfo1 | TransactionDescriptionResponseInfo1Dict]
