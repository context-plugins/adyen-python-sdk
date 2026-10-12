from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DklocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The 4-10 digits bank account number (Kontonummer) (without separators or whitespace)."""

    bank_code: str = Field(alias="bankCode")
    """The 4-digit bank code (Registreringsnummer) (without separators or whitespace)."""

    type_: Literal["dkLocal"] = Field(default="dkLocal", alias="type")
    """**dkLocal**"""


class DklocalAccountIdentificationDict(TypedDict):
    account_number: str
    bank_code: str
    type_: Literal["dkLocal"]
