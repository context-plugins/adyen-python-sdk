from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class SglocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, SGLocalAccountIdentification1."""

    type_: Literal["sgLocal"] = Field(default="sgLocal", alias="type")

    account_number: str = Field(alias="accountNumber")
    """The 4- to 19-digit bank account number, without separators or whitespace."""

    bic: str
    """The bank's 8- or 11-character BIC or SWIFT code."""


class SglocalAccountIdentification1Dict(TypedDict):
    type_: NotRequired[Literal["sgLocal"]]
    account_number: str
    bic: str
