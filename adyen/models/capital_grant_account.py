from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capital_balance import CapitalBalance, CapitalBalanceDict
from .grant_limit import GrantLimit, GrantLimitDict


class CapitalGrantAccount(SdkBaseModel):
    balances: Optional[list[CapitalBalance]] = UNSET
    """The balances of the grant account."""

    funding_balance_account_id: Optional[str] = Field(default=UNSET, alias="fundingBalanceAccountId")
    """The unique identifier of the balance account used to fund the grant."""

    id: Optional[str] = UNSET
    """The identifier of the grant account."""

    limits: Optional[list[GrantLimit]] = UNSET
    """The limits of the grant account."""


class CapitalGrantAccountDict(TypedDict):
    balances: NotRequired[list[CapitalBalance | CapitalBalanceDict]]
    funding_balance_account_id: NotRequired[str]
    id: NotRequired[str]
    limits: NotRequired[list[GrantLimit | GrantLimitDict]]
