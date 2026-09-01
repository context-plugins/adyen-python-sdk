from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class NolocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, NOLocalAccountIdentification1."""

    type_: Literal["noLocal"] = Field(default="noLocal", alias="type")

    account_number: str = Field(alias="accountNumber")
    """The 11-digit bank account number, without separators or whitespace."""


class NolocalAccountIdentification1Dict(TypedDict):
    type_: NotRequired[Literal["noLocal"]]
    account_number: str
