from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Name2(SdkBaseModel):
    """The name of the shopper."""

    first_name: str = Field(alias="firstName")
    """The first name."""

    last_name: str = Field(alias="lastName")
    """The last name."""


class Name2Dict(TypedDict):
    first_name: str
    last_name: str
