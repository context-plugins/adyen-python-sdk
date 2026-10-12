from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AulocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The bank account number, without separators or whitespace."""

    bsb_code: str = Field(alias="bsbCode")
    """The 6-digit `Bank State Branch (BSB) code <https://en.wikipedia.org/wiki/Bank_state_branch>`__, without
    separators or whitespace."""

    type_: Literal["auLocal"] = Field(default="auLocal", alias="type")
    """**auLocal**"""


class AulocalAccountIdentificationDict(TypedDict):
    account_number: str
    bsb_code: str
    type_: Literal["auLocal"]
