from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class SelocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The 7- to 10-digit bank account number (`Bankkontonummer <https://sv.wikipedia.org/wiki/Bankkonto>`__), without
    the clearing number, separators, or whitespace."""

    clearing_number: str = Field(alias="clearingNumber")
    """The 4- to 5-digit clearing number (`Clearingnummer <https://sv.wikipedia.org/wiki/Clearingnummer>`__), without
    separators or whitespace."""

    type_: Literal["seLocal"] = Field(default="seLocal", alias="type")
    """**seLocal**"""


class SelocalAccountIdentificationDict(TypedDict):
    account_number: str
    clearing_number: str
    type_: NotRequired[Literal["seLocal"]]
