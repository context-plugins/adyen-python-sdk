from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capital_balance import CapitalBalance, CapitalBalanceDict
from .grant_limit1 import GrantLimit1, GrantLimit1Dict


class GrantAccount(SdkBaseModel):
    balances: Optional[list[CapitalBalance]] = UNSET
    """Contains the sum of the balances of all grants tracked by this grant account. The balances are separated by
    currency."""

    funding_balance_account_id: Optional[str] = Field(default=UNSET, alias="fundingBalanceAccountId")
    """The unique identifier of the balance account used to fund the grant."""

    id: Optional[str] = UNSET
    """The unique identifier of the grant account."""

    limits: Optional[list[GrantLimit1]] = UNSET
    """Contains the maximum amount of funds that you can disburse for grants."""


class GrantAccountDict(TypedDict):
    balances: NotRequired[list[CapitalBalance | CapitalBalanceDict]]
    funding_balance_account_id: NotRequired[str]
    id: NotRequired[str]
    limits: NotRequired[list[GrantLimit1 | GrantLimit1Dict]]
