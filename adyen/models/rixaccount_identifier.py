from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RixaccountIdentifier(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The account number of the bank account."""

    clearing_number: str = Field(alias="clearingNumber")
    """The 4- to 5-digit clearing number, without separators or whitespace."""


class RixaccountIdentifierDict(TypedDict):
    account_number: str
    clearing_number: str
