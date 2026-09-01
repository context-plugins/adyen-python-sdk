from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.account_identification import AccountIdentification, AccountIdentificationDict


class BankAccount11(SdkBaseModel):
    """Contains information about the bank account."""

    account_identification: AccountIdentification = Field(alias="accountIdentification")
    """Contains the bank account details. The fields required in this object depend on the country of the bank account
    and the currency of the transfer."""


class BankAccount11Dict(TypedDict):
    account_identification: AccountIdentification | AccountIdentificationDict
