from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class HulocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, HULocalAccountIdentification1."""

    type_: str = Field(default="huLocal", alias="type")
    """**huLocal**"""

    account_number: str = Field(alias="accountNumber")
    """The 24-digit bank account number, without separators or whitespace."""


class HulocalAccountIdentification1Dict(TypedDict):
    type_: str
    account_number: str
