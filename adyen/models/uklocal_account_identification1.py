from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UklocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, UKLocalAccountIdentification1."""

    type_: Literal["ukLocal"] = Field(default="ukLocal", alias="type")

    account_number: str = Field(alias="accountNumber")
    """The 8-digit bank account number, without separators or whitespace."""

    sort_code: str = Field(alias="sortCode")
    """The 6-digit `sort code <https://en.wikipedia.org/wiki/Sort_code>`__, without separators or whitespace."""


class UklocalAccountIdentification1Dict(TypedDict):
    type_: NotRequired[Literal["ukLocal"]]
    account_number: str
    sort_code: str
