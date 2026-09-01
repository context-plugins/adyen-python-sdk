from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Name3(SdkBaseModel):
    first_name: str = Field(alias="firstName")
    """The individual's first name. Must not be blank."""

    infix: Optional[str] = UNSET
    """The infix in the individual's name, if any."""

    last_name: str = Field(alias="lastName")
    """The individual's last name. Must not be blank."""


class Name3Dict(TypedDict):
    first_name: str
    infix: NotRequired[str]
    last_name: str
