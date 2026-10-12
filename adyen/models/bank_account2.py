from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.account_identification2 import AccountIdentification2, AccountIdentification2Dict


class BankAccount2(SdkBaseModel):
    account_identification: AccountIdentification2 = Field(alias="accountIdentification")
    """Contains the bank account details. The fields required in this object depend on the country of the bank account
    and the currency of the transfer."""


class BankAccount2Dict(TypedDict):
    account_identification: AccountIdentification2Dict
