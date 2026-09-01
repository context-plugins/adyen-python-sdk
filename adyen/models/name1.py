from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Name1(SdkBaseModel):
    """The name of the person funding the money."""

    first_name: str = Field(alias="firstName")
    """The first name."""

    last_name: str = Field(alias="lastName")
    """The last name."""


class Name1Dict(TypedDict):
    first_name: str
    last_name: str
