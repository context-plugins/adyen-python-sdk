from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_info1 import TransactionDescriptionInfo1, TransactionDescriptionInfo1Dict


class GenericPmWithTdiUpdateInfo9(SdkBaseModel):
    """Details to provide if ``type`` is **interac_card**."""

    transaction_description: Optional[TransactionDescriptionInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""


class GenericPmWithTdiUpdateInfo9Dict(TypedDict):
    transaction_description: NotRequired[TransactionDescriptionInfo1Dict]
