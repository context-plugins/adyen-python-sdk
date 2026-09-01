from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_identifiers1 import AccountIdentifiers1, AccountIdentifiers1Dict
from .account_party import AccountParty, AccountPartyDict
from .enums.account_type11 import AccountType11OrStr


class VerifiedAccount(SdkBaseModel):
    account_id: str = Field(alias="accountId")
    """The unique identifier for the bank account."""

    account_name: str = Field(alias="accountName")
    """The name of the bank account. This name is assigned by the banking institution, and it describes the type of bank
    account."""

    account_number: str = Field(alias="accountNumber")
    """The account number of the bank account."""

    account_type: AccountType11OrStr = Field(alias="accountType")
    """The type of the bank account. Possible values are **CURRENT**, **SAVINGS**, **BUSINESS**, **CREDIT_CARD**,
    **LOAN**, **UNKNOWN**."""

    bank_name: Optional[str] = Field(default=UNSET, alias="bankName")
    """The name of the banking institution where the bank account is held."""

    currency: str
    """The currency of the funds in the bank account."""

    identifiers: AccountIdentifiers1
    """Contains various codes and details used to uniquely identify the bank account across different regions."""

    parties: list[AccountParty]
    """Contains details of all parties associated with the report."""


class VerifiedAccountDict(TypedDict):
    account_id: str
    account_name: str
    account_number: str
    account_type: AccountType11OrStr
    bank_name: NotRequired[str]
    currency: str
    identifiers: AccountIdentifiers1 | AccountIdentifiers1Dict
    parties: list[AccountParty | AccountPartyDict]
