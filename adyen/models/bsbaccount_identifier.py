from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BsbaccountIdentifier(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The account number of the bank account."""

    bsb_code: str = Field(alias="bsbCode")
    """The BSB (Bank-State-Branch) code."""


class BsbaccountIdentifierDict(TypedDict):
    account_number: str
    bsb_code: str
