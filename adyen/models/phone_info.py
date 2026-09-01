from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PhoneInfo(SdkBaseModel):
    hashed_number: Optional[str] = Field(default=UNSET, alias="hashedNumber")
    """The hashed value of the phone number used to provision the network token."""

    last_four_digits: Optional[str] = Field(default=UNSET, alias="lastFourDigits")
    """The last four digits of the phone number used to provision the network token."""

    number: Optional[str] = UNSET
    """The full phone number of the device used to provision the network token."""


class PhoneInfoDict(TypedDict):
    hashed_number: NotRequired[str]
    last_four_digits: NotRequired[str]
    number: NotRequired[str]
