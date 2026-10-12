from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction1 import Transaction1, Transaction1Dict


class AccountTransactionList(SdkBaseModel):
    account_code: Optional[str] = Field(default=UNSET, alias="accountCode")
    """The code of the account."""

    has_next_page: Optional[bool] = Field(default=UNSET, alias="hasNextPage")
    """Indicates whether there is a next page of transactions available."""

    transactions: Optional[list[Transaction1]] = UNSET
    """The list of transactions."""


class AccountTransactionListDict(TypedDict):
    account_code: NotRequired[str]
    has_next_page: NotRequired[bool]
    transactions: NotRequired[list[Transaction1Dict]]
