from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MigratedAccounts(SdkBaseModel):
    account_code: Optional[str] = Field(default=UNSET, alias="accountCode")
    """The unique identifier of the account of the migrated account holder in the classic integration."""

    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """The unique identifier of the account of the migrated account holder in the balance platform."""


class MigratedAccountsDict(TypedDict):
    account_code: NotRequired[str]
    balance_account_id: NotRequired[str]
