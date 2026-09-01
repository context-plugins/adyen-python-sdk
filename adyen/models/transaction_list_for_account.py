from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransactionListForAccount(SdkBaseModel):
    account_code: str = Field(alias="accountCode")
    """The account for which to retrieve the transactions."""

    page: int
    """The page of transactions to retrieve. Each page lists fifty (50) transactions. The most recent transactions are
    included on page 1."""


class TransactionListForAccountDict(TypedDict):
    account_code: str
    page: int
