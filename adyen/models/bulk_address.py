from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BulkAddress(SdkBaseModel):
    city: Optional[str] = UNSET
    """The name of the city."""

    company: Optional[str] = UNSET
    """The name of the company."""

    country: str
    """The two-character ISO-3166-1 alpha-2 country code. For example, **US**."""

    email: Optional[str] = UNSET
    """The email address."""

    house_number_or_name: Optional[str] = Field(default=UNSET, alias="houseNumberOrName")
    """The house number or name."""

    line1: Optional[str] = UNSET
    """The name of the street and the number of the building.

    For example: **Simon Carmiggeltstraat 6-50**."""

    line2: Optional[str] = UNSET
    """Additional information about the delivery address. For example, an apartment number."""

    line3: Optional[str] = UNSET
    """Additional information about the delivery address."""

    mobile: Optional[str] = UNSET
    """The full telephone number."""

    name: Optional[str] = UNSET
    """The recipient’s name (person or contact), for example ‘John Doe’."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The postal code.

    Maximum length:

    * 5 digits for addresses in the US.

    * 10 characters for all other countries."""

    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    """The two-letter ISO 3166-2 state or province code.

    Maximum length: 2 characters for addresses in the US."""

    street: Optional[str] = UNSET
    """The streetname of the house."""


class BulkAddressDict(TypedDict):
    city: NotRequired[str]
    company: NotRequired[str]
    country: str
    email: NotRequired[str]
    house_number_or_name: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    mobile: NotRequired[str]
    name: NotRequired[str]
    postal_code: NotRequired[str]
    state_or_province: NotRequired[str]
    street: NotRequired[str]
