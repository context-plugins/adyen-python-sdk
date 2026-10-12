from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NolocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, NOLocalAccountIdentification1."""

    type_: str = Field(default="noLocal", alias="type")
    """**noLocal**"""

    account_number: str = Field(alias="accountNumber")
    """The 11-digit bank account number, without separators or whitespace."""


class NolocalAccountIdentification1Dict(TypedDict):
    type_: str
    account_number: str
