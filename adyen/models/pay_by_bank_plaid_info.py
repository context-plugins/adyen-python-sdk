from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_info1 import TransactionDescriptionInfo1, TransactionDescriptionInfo1Dict


class PayByBankPlaidInfo(SdkBaseModel):
    logo: Optional[str] = UNSET
    """Merchant logo (max. size 150kB). Format: Base64-encoded string."""

    transaction_description: Optional[TransactionDescriptionInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""


class PayByBankPlaidInfoDict(TypedDict):
    logo: NotRequired[str]
    transaction_description: NotRequired[TransactionDescriptionInfo1Dict]
