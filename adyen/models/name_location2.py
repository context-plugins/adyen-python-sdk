from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NameLocation2(SdkBaseModel):
    """Contains the name and location of the merchant."""

    city: Optional[str] = UNSET
    """The city where the merchant is located."""

    country: Optional[str] = UNSET
    """The country where the merchant is located in `three-letter country code
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`__ format."""

    country_of_origin: Optional[str] = Field(default=UNSET, alias="countryOfOrigin")
    """The home country in `three-digit country code <https://en.wikipedia.org/wiki/ISO_3166-1_numeric>`__ format, used
    for government-controlled merchants such as embassies."""

    name: Optional[str] = UNSET
    """The name of the merchant's shop or service."""

    raw_data: Optional[str] = Field(default=UNSET, alias="rawData")
    """The raw data."""

    state: Optional[str] = UNSET
    """The state where the merchant is located."""


class NameLocation2Dict(TypedDict):
    city: NotRequired[str]
    country: NotRequired[str]
    country_of_origin: NotRequired[str]
    name: NotRequired[str]
    raw_data: NotRequired[str]
    state: NotRequired[str]
