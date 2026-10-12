from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.account_type2 import AccountType2, AccountType2OrStr


class CalocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The 5- to 12-digit bank account number, without separators or whitespace."""

    account_type: AccountType2OrStr = Field(default=AccountType2.CHECKING, alias="accountType")
    """The bank account type.

    Possible values: **checking** or **savings**. Defaults to **checking**."""

    institution_number: str = Field(alias="institutionNumber")
    """The 3-digit institution number, without separators or whitespace."""

    transit_number: str = Field(alias="transitNumber")
    """The 5-digit transit number, without separators or whitespace."""

    type_: Literal["caLocal"] = Field(default="caLocal", alias="type")
    """**caLocal**"""


class CalocalAccountIdentificationDict(TypedDict):
    account_number: str
    account_type: NotRequired[AccountType2OrStr]
    institution_number: str
    transit_number: str
    type_: Literal["caLocal"]
