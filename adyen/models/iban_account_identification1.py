from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IbanAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, IbanAccountIdentification1."""

    type_: str = Field(default="iban", alias="type")
    """**iban**"""

    bic: Optional[str] = UNSET
    """The bank's 8- or 11-character BIC or SWIFT code."""

    iban: str
    """The international bank account number as defined in the `ISO-13616 <https://www.iso.org/standard/81090.html>`__
    standard."""


class IbanAccountIdentification1Dict(TypedDict):
    type_: str
    bic: NotRequired[str]
    iban: str
