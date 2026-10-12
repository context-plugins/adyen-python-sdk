from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict


class MerchantBalance(SdkBaseModel):
    available_fund: Optional[Amount17] = Field(default=UNSET, alias="availableFund")
    deposit: Optional[Amount17] = UNSET
    merchant_account: Optional[str] = Field(default=UNSET, alias="merchantAccount")
    next_payout: Optional[Amount17] = Field(default=UNSET, alias="nextPayout")
    pending_balance: Optional[Amount17] = Field(default=UNSET, alias="pendingBalance")
    reserve: Optional[Amount17] = UNSET


class MerchantBalanceDict(TypedDict):
    available_fund: NotRequired[Amount17Dict]
    deposit: NotRequired[Amount17Dict]
    merchant_account: NotRequired[str]
    next_payout: NotRequired[Amount17Dict]
    pending_balance: NotRequired[Amount17Dict]
    reserve: NotRequired[Amount17Dict]
