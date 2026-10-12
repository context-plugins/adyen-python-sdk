from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CzlocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, CZLocalAccountIdentification1."""

    type_: str = Field(default="czLocal", alias="type")
    """**czLocal**"""

    account_number: str = Field(alias="accountNumber")
    """The 2- to 16-digit bank account number (Číslo účtu) in the following format:

    - The optional prefix (předčíslí).

    - The required second part (základní část) which must be at least two non-zero digits.

    Examples:

    - **19-123457** (with prefix)

    - **123457** (without prefix)

    - **000019-0000123457** (with prefix, normalized)

    - **000000-0000123457** (without prefix, normalized)"""

    bank_code: str = Field(alias="bankCode")
    """The 4-digit bank code (Kód banky), without separators or whitespace."""


class CzlocalAccountIdentification1Dict(TypedDict):
    type_: str
    account_number: str
    bank_code: str
