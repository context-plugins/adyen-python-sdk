from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address5(SdkBaseModel):
    """The billing address associated with the stored payment method."""

    city: str
    """The name of the city. Maximum length: 3000 characters."""

    country: str
    """The two-character ISO-3166-1 alpha-2 country code. For example, **US**.
    > If you don't know the country or are not collecting the country from the shopper, provide ``country`` as
        ``ZZ``."""

    house_number_or_name: str = Field(alias="houseNumberOrName")
    """The number or name of the house. Maximum length: 3000 characters."""

    postal_code: str = Field(alias="postalCode")
    """A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other
    countries."""

    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    """The two-character ISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada.
    > Required for the US and Canada."""

    street: str
    """The name of the street. Maximum length: 3000 characters.
    > The house number should not be included in this field; it should be separately provided via
        ``houseNumberOrName``."""


class Address5Dict(TypedDict):
    city: str
    country: str
    house_number_or_name: str
    postal_code: str
    state_or_province: NotRequired[str]
    street: str
