from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type410 import Type410OrStr


class Phone11(SdkBaseModel):
    """The phone number where the one-time password (OTP) is sent.

    This object must have:

    * A ``type`` set to **mobile**.

    * A ``number`` with a valid country code.

    * A ``number`` with more than 4 digits, excluding the country code.

    >Make sure to verify that the card user owns the phone number."""

    number: str
    """The full phone number provided as a single string. For example, **"0031 6 11 22 33 44"**, **"+316/1122-3344"**,

     or **"(0031) 611223344"**."""

    type_: Type410OrStr = Field(alias="type")
    """Type of phone number. Possible values: **Landline**, **Mobile**."""


class Phone11Dict(TypedDict):
    number: str
    type_: Type410OrStr
