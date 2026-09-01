from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .phone_number1 import PhoneNumber1, PhoneNumber1Dict


class Support1(SdkBaseModel):
    """Support information for the legal entity. Required if you have a platform setup."""

    email: Optional[str] = UNSET
    """The support email address of the legal entity. Required if you have a platform setup."""

    phone: Optional[PhoneNumber1] = UNSET
    """The support phone number of the legal entity. Required if you have a platform setup."""


class Support1Dict(TypedDict):
    email: NotRequired[str]
    phone: NotRequired[PhoneNumber1 | PhoneNumber1Dict]
