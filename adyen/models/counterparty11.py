from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_holder11 import AccountHolder11, AccountHolder11Dict
from .account_identification1 import AccountIdentification1, AccountIdentification1Dict


class Counterparty11(SdkBaseModel):
    """Contains information about the party that receives the payment funds."""

    account_holder: AccountHolder11 = Field(alias="accountHolder")
    """Contains the full name of the person or entity that receives the payment funds)."""

    account_identification: AccountIdentification1 = Field(alias="accountIdentification")
    """Contains the account number to which the payment funds are sent."""


class Counterparty11Dict(TypedDict):
    account_holder: AccountHolder11Dict
    account_identification: AccountIdentification1Dict
