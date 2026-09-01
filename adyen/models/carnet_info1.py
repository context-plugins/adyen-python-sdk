from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_info1 import TransactionDescriptionInfo1, TransactionDescriptionInfo1Dict


class CarnetInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **carnet**."""

    add_mcc_acronym: Optional[bool] = Field(default=UNSET, alias="addMccAcronym")
    """Indicates whether to add the MCC acronym to the merchant name for Prosa acquirer in Mexico. When set to **true**,
    the MCC acronym is automatically appended to the merchant name. Default: **false**."""

    transaction_description: Optional[TransactionDescriptionInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""


class CarnetInfo1Dict(TypedDict):
    add_mcc_acronym: NotRequired[bool]
    transaction_description: NotRequired[TransactionDescriptionInfo1 | TransactionDescriptionInfo1Dict]
