from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type410 import Type410OrStr


class Phone4(SdkBaseModel):
    number: str
    """The full phone number provided as a single string. For example, **"0031 6 11 22 33 44"**, **"+316/1122-3344"**,

     or **"(0031) 611223344"**."""

    type_: Type410OrStr = Field(alias="type")
    """Type of phone number. Possible values: **Landline**, **Mobile**."""


class Phone4Dict(TypedDict):
    number: str
    type_: Type410OrStr
