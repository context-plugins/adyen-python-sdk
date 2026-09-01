from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_response_info1 import (
    TransactionDescriptionResponseInfo1,
    TransactionDescriptionResponseInfo1Dict,
)


class DinersResponseInfo1(SdkBaseModel):
    """**diners** details"""

    mid_number: Optional[str] = Field(default=UNSET, alias="midNumber")
    """MID (Merchant ID) number."""

    reuse_mid_number: Optional[bool] = Field(default=UNSET, alias="reuseMidNumber")
    """Indicates whether the JCB Merchant ID is reused from a previously configured JCB payment method."""

    service_level: Optional[str] = Field(default=UNSET, alias="serviceLevel")
    """The service level (settlement type) of this payment method. Possible values:
     * **noContract**: Adyen holds the contract with JCB.
     * **gatewayContract**: JCB receives the settlement and handles disputes, then pays out to you or your sub-merchant
            directly."""

    transaction_description: Optional[TransactionDescriptionResponseInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description."""


class DinersResponseInfo1Dict(TypedDict):
    mid_number: NotRequired[str]
    reuse_mid_number: NotRequired[bool]
    service_level: NotRequired[str]
    transaction_description: NotRequired[TransactionDescriptionResponseInfo1 | TransactionDescriptionResponseInfo1Dict]
