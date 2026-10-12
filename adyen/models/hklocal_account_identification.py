from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class HklocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The 9- to 17-digit bank account number, without separators or whitespace. Starts with the 3-digit branch code."""

    clearing_code: str = Field(alias="clearingCode")
    """The 3-digit clearing code, without separators or whitespace."""

    type_: Literal["hkLocal"] = Field(default="hkLocal", alias="type")
    """**hkLocal**"""


class HklocalAccountIdentificationDict(TypedDict):
    account_number: str
    clearing_code: str
    type_: Literal["hkLocal"]
