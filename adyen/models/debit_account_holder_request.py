from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict
from .split1 import Split1, Split1Dict


class DebitAccountHolderRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the account holder."""

    amount: Amount
    """The amount to be debited from the account holder's bank account."""

    bank_account_uuid: str = Field(alias="bankAccountUUID")
    """The Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account."""

    description: Optional[str] = UNSET
    """A description of the direct debit. Maximum length: 35 characters.

    Allowed characters: **a-z**, **A-Z**, **0-9**, and special characters **/?:().,'+ ";**."""

    merchant_account: str = Field(alias="merchantAccount")
    """Your merchant account."""

    splits: list[Split1]
    """Contains instructions on how to split the funds between the accounts in your platform. The request must have at
    least one split item."""


class DebitAccountHolderRequestDict(TypedDict):
    account_holder_code: str
    amount: Amount | AmountDict
    bank_account_uuid: str
    description: NotRequired[str]
    merchant_account: str
    splits: list[Split1 | Split1Dict]
