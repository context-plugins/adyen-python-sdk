from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AulocalAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, AULocalAccountIdentification1."""

    type_: Literal["auLocal"] = Field(default="auLocal", alias="type")

    account_number: str = Field(alias="accountNumber")
    """The bank account number, without separators or whitespace."""

    bsb_code: str = Field(alias="bsbCode")
    """The 6-digit `Bank State Branch (BSB) code <https://en.wikipedia.org/wiki/Bank_state_branch>`__, without
    separators or whitespace."""


class AulocalAccountIdentification1Dict(TypedDict):
    type_: NotRequired[Literal["auLocal"]]
    account_number: str
    bsb_code: str
