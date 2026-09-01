from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class HulocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, HULocalAccountIdentification1."""

    type_: Literal["huLocal"] = Field(default="huLocal", alias="type")

    account_number: str = Field(alias="accountNumber")
    """The 24-digit bank account number, without separators or whitespace."""


class HulocalAccountIdentification1Dict(TypedDict):
    type_: NotRequired[Literal["huLocal"]]
    account_number: str
