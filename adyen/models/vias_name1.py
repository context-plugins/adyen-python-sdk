from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.gender import GenderOrStr


class ViasName1(SdkBaseModel):
    """The name of the person."""

    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    """The first name."""

    gender: Optional[GenderOrStr] = UNSET
    """The gender. >The following values are permitted: ``MALE``, ``FEMALE``, ``UNKNOWN``."""

    infix: Optional[str] = UNSET
    """The name's infix, if applicable. >A maximum length of twenty (20) characters is imposed."""

    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    """The last name."""


class ViasName1Dict(TypedDict):
    first_name: NotRequired[str]
    gender: NotRequired[GenderOrStr]
    infix: NotRequired[str]
    last_name: NotRequired[str]
