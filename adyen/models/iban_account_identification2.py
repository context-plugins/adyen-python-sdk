from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class IbanAccountIdentification2(SdkBaseModel):
    """All Of AccountIdentification, IbanAccountIdentification2."""

    type_: Literal["iban"] = Field(default="iban", alias="type")

    iban: str
    """The IBAN of the bank account."""


class IbanAccountIdentification2Dict(TypedDict):
    type_: NotRequired[Literal["iban"]]
    iban: str
