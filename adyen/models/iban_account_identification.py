from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IbanAccountIdentification(SdkBaseModel):
    bic: Optional[str] = UNSET
    """The bank's 8- or 11-character BIC or SWIFT code."""

    iban: str
    """The international bank account number as defined in the `ISO-13616 <https://www.iso.org/standard/81090.html>`__
    standard."""

    type_: Literal["iban"] = Field(default="iban", alias="type")
    """**iban**"""


class IbanAccountIdentificationDict(TypedDict):
    bic: NotRequired[str]
    iban: str
    type_: Literal["iban"]
