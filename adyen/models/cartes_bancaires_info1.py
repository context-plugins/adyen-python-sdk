from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_info1 import TransactionDescriptionInfo1, TransactionDescriptionInfo1Dict


class CartesBancairesInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **cartebancaire**."""

    siret: str
    """Cartes Bancaires SIRET. Format: 14 digits."""

    transaction_description: Optional[TransactionDescriptionInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""


class CartesBancairesInfo1Dict(TypedDict):
    siret: str
    transaction_description: NotRequired[TransactionDescriptionInfo1 | TransactionDescriptionInfo1Dict]
