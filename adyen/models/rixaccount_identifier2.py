from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RixaccountIdentifier2(SdkBaseModel):
    """Identifiers relevant for the Rix (Russian Interbank eXchange) system, used for interbank payments within
    Russia."""

    account_number: str = Field(alias="accountNumber")
    """The account number of the bank account."""

    clearing_number: str = Field(alias="clearingNumber")
    """The 4- to 5-digit clearing number, without separators or whitespace."""


class RixaccountIdentifier2Dict(TypedDict):
    account_number: str
    clearing_number: str
