from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BacsaccountIdentifier(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The account number of the bank account."""

    sort_code: str = Field(alias="sortCode")
    """A number that identifies the specific bank and branch where a UK bank account is held."""


class BacsaccountIdentifierDict(TypedDict):
    account_number: str
    sort_code: str
