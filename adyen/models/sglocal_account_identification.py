from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.type82 import Type82, Type82OrStr


class SglocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The 4- to 19-digit bank account number, without separators or whitespace."""

    bic: str
    """The bank's 8- or 11-character BIC or SWIFT code."""

    type_: Type82OrStr = Field(default=Type82.SG_LOCAL, alias="type")
    """**sgLocal**"""


class SglocalAccountIdentificationDict(TypedDict):
    account_number: str
    bic: str
    type_: NotRequired[Type82OrStr]
