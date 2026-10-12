from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.account_type2 import AccountType2OrStr


class UslocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, USLocalAccountIdentification1."""

    type_: str = Field(default="usLocal", alias="type")
    """**usLocal**"""

    account_number: str = Field(alias="accountNumber")
    """The bank account number, without separators or whitespace."""

    account_type: Optional[AccountType2OrStr] = Field(default=UNSET, alias="accountType")
    """The bank account type.

    Possible values: **checking** or **savings**. Defaults to **checking**."""

    routing_number: str = Field(alias="routingNumber")
    """The 9-digit `routing number <https://en.wikipedia.org/wiki/ABA_routing_transit_number>`__, without separators or
    whitespace."""


class UslocalAccountIdentification1Dict(TypedDict):
    type_: str
    account_number: str
    account_type: NotRequired[AccountType2OrStr]
    routing_number: str
