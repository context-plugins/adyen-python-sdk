from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Name21(SdkBaseModel):
    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    """The first name."""

    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    """The last name."""


class Name21Dict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
