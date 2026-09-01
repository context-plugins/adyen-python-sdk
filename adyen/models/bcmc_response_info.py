from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_response_info1 import (
    TransactionDescriptionResponseInfo1,
    TransactionDescriptionResponseInfo1Dict,
)


class BcmcResponseInfo(SdkBaseModel):
    enable_bcmc_mobile: Optional[bool] = Field(default=UNSET, alias="enableBcmcMobile")
    """Indicates if `Bancontact mobile <https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile>`__ is
    enabled."""

    transaction_description: Optional[TransactionDescriptionResponseInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description."""


class BcmcResponseInfoDict(TypedDict):
    enable_bcmc_mobile: NotRequired[bool]
    transaction_description: NotRequired[TransactionDescriptionResponseInfo1 | TransactionDescriptionResponseInfo1Dict]
