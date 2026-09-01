from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .merchant_balance import MerchantBalance, MerchantBalanceDict


class CompanyBalances(SdkBaseModel):
    merchant_balances_overview: Optional[list[MerchantBalance]] = Field(default=UNSET, alias="merchantBalancesOverview")


class CompanyBalancesDict(TypedDict):
    merchant_balances_overview: NotRequired[list[MerchantBalance | MerchantBalanceDict]]
