from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_account_id import LoyaltyAccountId, LoyaltyAccountIdDict
from .transaction_idtype import TransactionIdtype, TransactionIdtypeDict


class LoyaltyAccountReq(SdkBaseModel):
    card_acquisition_reference: Optional[TransactionIdtype] = Field(default=UNSET, alias="CardAcquisitionReference")
    """Identification of a transaction for the Sale System or the POI System."""

    loyalty_account_id: Optional[LoyaltyAccountId] = Field(default=UNSET, alias="LoyaltyAccountID")
    """Identification of a Loyalty account. In the Payment Request message, it allows to identify the loyalty account by
    the Sale Terminal instead of the POI Terminal (e.g. because the account identification is a bar-code read by the
    Cashier on a scanner device)."""


class LoyaltyAccountReqDict(TypedDict):
    card_acquisition_reference: NotRequired[TransactionIdtype | TransactionIdtypeDict]
    loyalty_account_id: NotRequired[LoyaltyAccountId | LoyaltyAccountIdDict]
