from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UklocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The 8-digit bank account number, without separators or whitespace."""

    sort_code: str = Field(alias="sortCode")
    """The 6-digit `sort code <https://en.wikipedia.org/wiki/Sort_code>`__, without separators or whitespace."""

    type_: Literal["ukLocal"] = Field(default="ukLocal", alias="type")
    """**ukLocal**"""


class UklocalAccountIdentificationDict(TypedDict):
    account_number: str
    sort_code: str
    type_: NotRequired[Literal["ukLocal"]]
