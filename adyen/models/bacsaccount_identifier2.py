from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BacsaccountIdentifier2(SdkBaseModel):
    """Identifiers relevant for Bankers' Automated Clearing Services (BACS) payments, primarily used in the United
    Kingdom."""

    account_number: str = Field(alias="accountNumber")
    """The account number of the bank account."""

    sort_code: str = Field(alias="sortCode")
    """A number that identifies the specific bank and branch where a UK bank account is held."""


class BacsaccountIdentifier2Dict(TypedDict):
    account_number: str
    sort_code: str
