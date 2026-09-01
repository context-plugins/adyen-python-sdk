from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShopperName2(SdkBaseModel):
    """The shopper's full name."""

    first_name: str = Field(alias="firstName")
    """The first name."""

    last_name: str = Field(alias="lastName")
    """The last name."""


class ShopperName2Dict(TypedDict):
    first_name: str
    last_name: str
