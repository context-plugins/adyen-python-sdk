from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SelocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, SELocalAccountIdentification1."""

    type_: str = Field(default="seLocal", alias="type")
    """**seLocal**"""

    account_number: str = Field(alias="accountNumber")
    """The 7- to 10-digit bank account number (`Bankkontonummer <https://sv.wikipedia.org/wiki/Bankkonto>`__), without
    the clearing number, separators, or whitespace."""

    clearing_number: str = Field(alias="clearingNumber")
    """The 4- to 5-digit clearing number (`Clearingnummer <https://sv.wikipedia.org/wiki/Clearingnummer>`__), without
    separators or whitespace."""


class SelocalAccountIdentification1Dict(TypedDict):
    type_: str
    account_number: str
    clearing_number: str
