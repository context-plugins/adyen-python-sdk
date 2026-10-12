from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .balance_account_base import BalanceAccountBase, BalanceAccountBaseDict


class PaginatedBalanceAccountsResponse(SdkBaseModel):
    balance_accounts: list[BalanceAccountBase] = Field(alias="balanceAccounts")
    """List of balance accounts."""

    has_next: bool = Field(alias="hasNext")
    """Indicates whether there are more items on the next page."""

    has_previous: bool = Field(alias="hasPrevious")
    """Indicates whether there are more items on the previous page."""


class PaginatedBalanceAccountsResponseDict(TypedDict):
    balance_accounts: list[BalanceAccountBaseDict]
    has_next: bool
    has_previous: bool
