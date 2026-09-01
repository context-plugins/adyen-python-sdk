from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeleteBankAccountRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the Account Holder from which to delete the Bank Account(s)."""

    bank_account_uuids: list[str] = Field(alias="bankAccountUUIDs")
    """The code(s) of the Bank Accounts to be deleted."""


class DeleteBankAccountRequestDict(TypedDict):
    account_holder_code: str
    bank_account_uuids: list[str]
