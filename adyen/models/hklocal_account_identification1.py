from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class HklocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, HKLocalAccountIdentification1."""

    type_: Literal["hkLocal"] = Field(default="hkLocal", alias="type")

    account_number: str = Field(alias="accountNumber")
    """The 9- to 17-digit bank account number, without separators or whitespace. Starts with the 3-digit branch code."""

    clearing_code: str = Field(alias="clearingCode")
    """The 3-digit clearing code, without separators or whitespace."""


class HklocalAccountIdentification1Dict(TypedDict):
    type_: NotRequired[Literal["hkLocal"]]
    account_number: str
    clearing_code: str
