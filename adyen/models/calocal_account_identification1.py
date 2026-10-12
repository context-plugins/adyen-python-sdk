from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.account_type2 import AccountType2OrStr


class CalocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, CALocalAccountIdentification1."""

    type_: str = Field(default="caLocal", alias="type")
    """**caLocal**"""

    account_number: str = Field(alias="accountNumber")
    """The 5- to 12-digit bank account number, without separators or whitespace."""

    account_type: Optional[AccountType2OrStr] = Field(default=UNSET, alias="accountType")
    """The bank account type.

    Possible values: **checking** or **savings**. Defaults to **checking**."""

    institution_number: str = Field(alias="institutionNumber")
    """The 3-digit institution number, without separators or whitespace."""

    transit_number: str = Field(alias="transitNumber")
    """The 5-digit transit number, without separators or whitespace."""


class CalocalAccountIdentification1Dict(TypedDict):
    type_: str
    account_number: str
    account_type: NotRequired[AccountType2OrStr]
    institution_number: str
    transit_number: str
