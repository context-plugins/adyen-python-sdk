from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ViasAddress7(SdkBaseModel):
    """The address of the physical store where the account holder will process payments from."""

    city: Optional[str] = UNSET
    """The name of the city. Required if the ``houseNumberOrName``, ``street``, ``postalCode``, or ``stateOrProvince``
    are provided."""

    country: str
    """The two-character country code of the address in ISO-3166-1 alpha-2 format. For example, **NL**."""

    house_number_or_name: Optional[str] = Field(default=UNSET, alias="houseNumberOrName")
    """The number or name of the house."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The postal code. Required if the ``houseNumberOrName``, ``street``, ``city``, or ``stateOrProvince`` are
    provided.

    Maximum length:

    * 5 digits for addresses in the US.

    * 10 characters for all other countries."""

    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    """The abbreviation of the state or province. Required if the ``houseNumberOrName``, ``street``, ``city``, or
    ``postalCode`` are provided.

    Maximum length:

    * 2 characters for addresses in the US or Canada.

    * 3 characters for all other countries."""

    street: Optional[str] = UNSET
    """The name of the street. Required if the ``houseNumberOrName``, ``city``, ``postalCode``, or ``stateOrProvince``
    are provided."""


class ViasAddress7Dict(TypedDict):
    city: NotRequired[str]
    country: str
    house_number_or_name: NotRequired[str]
    postal_code: NotRequired[str]
    state_or_province: NotRequired[str]
    street: NotRequired[str]
