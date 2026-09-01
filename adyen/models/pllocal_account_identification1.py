from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class PllocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, PLLocalAccountIdentification1."""

    type_: Literal["plLocal"] = Field(default="plLocal", alias="type")

    account_number: str = Field(alias="accountNumber")
    """The 26-digit bank account number (`Numer rachunku <https://pl.wikipedia.org/wiki/Numer_Rachunku_Bankowego>`__),
    without separators or whitespace."""


class PllocalAccountIdentification1Dict(TypedDict):
    type_: NotRequired[Literal["plLocal"]]
    account_number: str
