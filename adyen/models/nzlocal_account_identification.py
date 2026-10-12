from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NzlocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The 15-16 digit bank account number. The first 2 digits are the bank number, the next 4 digits are the branch
    number, the next 7 digits are the account number, and the final 2-3 digits are the suffix."""

    type_: Literal["nzLocal"] = Field(default="nzLocal", alias="type")
    """**nzLocal**"""


class NzlocalAccountIdentificationDict(TypedDict):
    account_number: str
    type_: Literal["nzLocal"]
