from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PllocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The 26-digit bank account number (`Numer rachunku <https://pl.wikipedia.org/wiki/Numer_Rachunku_Bankowego>`__),
    without separators or whitespace."""

    type_: Literal["plLocal"] = Field(default="plLocal", alias="type")
    """**plLocal**"""


class PllocalAccountIdentificationDict(TypedDict):
    account_number: str
    type_: Literal["plLocal"]
