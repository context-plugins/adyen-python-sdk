from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.account_type2 import AccountType2OrStr


class UslocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The bank account number, without separators or whitespace."""

    account_type: Optional[AccountType2OrStr] = Field(default=UNSET, alias="accountType")
    """The bank account type.

    Possible values: **checking** or **savings**. Defaults to **checking**."""

    routing_number: str = Field(alias="routingNumber")
    """The 9-digit `routing number <https://en.wikipedia.org/wiki/ABA_routing_transit_number>`__, without separators or
    whitespace."""

    type_: Literal["usLocal"] = Field(default="usLocal", alias="type")
    """**usLocal**"""


class UslocalAccountIdentificationDict(TypedDict):
    account_number: str
    account_type: NotRequired[AccountType2OrStr]
    routing_number: str
    type_: NotRequired[Literal["usLocal"]]
