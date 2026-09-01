from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .detail_balance3 import DetailBalance3, DetailBalance3Dict


class AccountDetailBalance(SdkBaseModel):
    account_code: Optional[str] = Field(default=UNSET, alias="accountCode")
    """The code of the account that holds the balance."""

    detail_balance: Optional[DetailBalance3] = Field(default=UNSET, alias="detailBalance")
    """Details of the balance held by the account."""


class AccountDetailBalanceDict(TypedDict):
    account_code: NotRequired[str]
    detail_balance: NotRequired[DetailBalance3 | DetailBalance3Dict]
