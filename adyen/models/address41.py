from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address41(SdkBaseModel):
    """The business address. Required if the principal place of business is different from the ``registeredAddress``."""

    city: Optional[str] = UNSET
    """The name of the city. Required if ``stateOrProvince`` is provided.

    If you specify the city, you must also send ``postalCode`` and ``street``."""

    country: str
    """The two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The postal code. Required if ``stateOrProvince`` and/or ``city`` is provided.

    When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA."""

    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    """The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New
    Zealand.

    If you specify the state or province, you must also send ``city``, ``postalCode``, and ``street``."""

    street: Optional[str] = UNSET
    """The name of the street, and the house or building number. Required if ``stateOrProvince`` and/or ``city`` is
    provided."""

    street2: Optional[str] = UNSET
    """The apartment, unit, or suite number."""


class Address41Dict(TypedDict):
    city: NotRequired[str]
    country: str
    postal_code: NotRequired[str]
    state_or_province: NotRequired[str]
    street: NotRequired[str]
    street2: NotRequired[str]
