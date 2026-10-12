from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DklocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, DKLocalAccountIdentification1."""

    type_: str = Field(default="dkLocal", alias="type")
    """**dkLocal**"""

    account_number: str = Field(alias="accountNumber")
    """The 4-10 digits bank account number (Kontonummer) (without separators or whitespace)."""

    bank_code: str = Field(alias="bankCode")
    """The 4-digit bank code (Registreringsnummer) (without separators or whitespace)."""


class DklocalAccountIdentification1Dict(TypedDict):
    type_: str
    account_number: str
    bank_code: str
