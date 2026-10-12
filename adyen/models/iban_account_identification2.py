from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IbanAccountIdentification2(SdkBaseModel):
    """All Of AccountIdentification, IbanAccountIdentification2."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    iban: str
    """The IBAN of the bank account."""


class IbanAccountIdentification2Dict(TypedDict):
    type_: NotRequired[str]
    iban: str
