from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class NolocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The 11-digit bank account number, without separators or whitespace."""

    type_: Literal["noLocal"] = Field(default="noLocal", alias="type")
    """**noLocal**"""


class NolocalAccountIdentificationDict(TypedDict):
    account_number: str
    type_: NotRequired[Literal["noLocal"]]
