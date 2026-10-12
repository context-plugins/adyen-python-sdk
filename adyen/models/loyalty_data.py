from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_account_id1 import LoyaltyAccountId1, LoyaltyAccountId1Dict
from .transaction_idtype3 import TransactionIdtype3, TransactionIdtype3Dict


class LoyaltyData(SdkBaseModel):
    """In the Payment, Loyalty or Balance Inquiry Request message, it allows the Sale Terminal to send the
    identification of the loyalty account or an awarded amount or an amount to redeem to the loyalty account. Data
    related to a Loyalty program or account."""

    card_acquisition_reference: Optional[TransactionIdtype3] = Field(default=UNSET, alias="CardAcquisitionReference")
    """Reference to the last CardAcquisition, to use the same card. If the loyalty account ID comes from a previous
    CardAcquisition."""

    loyalty_account_id: Optional[LoyaltyAccountId1] = Field(default=UNSET, alias="LoyaltyAccountID")
    """Identification of a Loyalty account. If loyalty identification of the loyalty account is realised by the Sale
    System."""


class LoyaltyDataDict(TypedDict):
    card_acquisition_reference: NotRequired[TransactionIdtype3Dict]
    loyalty_account_id: NotRequired[LoyaltyAccountId1Dict]
