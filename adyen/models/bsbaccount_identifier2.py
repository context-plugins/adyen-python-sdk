from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BsbaccountIdentifier2(SdkBaseModel):
    """Identifiers relevant for Australian banking, specifically for BSB (Bank-State-Branch) numbers."""

    account_number: str = Field(alias="accountNumber")
    """The account number of the bank account."""

    bsb_code: str = Field(alias="bsbCode")
    """The BSB (Bank-State-Branch) code."""


class BsbaccountIdentifier2Dict(TypedDict):
    account_number: str
    bsb_code: str
