from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class HulocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The 24-digit bank account number, without separators or whitespace."""

    type_: Literal["huLocal"] = Field(default="huLocal", alias="type")
    """**huLocal**"""


class HulocalAccountIdentificationDict(TypedDict):
    account_number: str
    type_: NotRequired[Literal["huLocal"]]
