from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address11(SdkBaseModel):
    """The address details of the billing entity."""

    city: Optional[str] = UNSET
    """The name of the city."""

    company_name: Optional[str] = Field(default=UNSET, alias="companyName")
    """The name of the company."""

    country: Optional[str] = UNSET
    """The two-letter country code, in `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
    format."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The postal code."""

    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    """The state or province as defined in `ISO 3166-2 <https://www.iso.org/standard/72483.html>`__. For example, **ON**
    for Ontario, Canada.

    Applicable for the following countries:
    - Australia
    - Brazil
    - Canada
    - India
    - Mexico
    - New Zealand
    - United States"""

    street_address: Optional[str] = Field(default=UNSET, alias="streetAddress")
    """The name of the street, and the house or building number."""

    street_address2: Optional[str] = Field(default=UNSET, alias="streetAddress2")
    """Additional address details, if any."""


class Address11Dict(TypedDict):
    city: NotRequired[str]
    company_name: NotRequired[str]
    country: NotRequired[str]
    postal_code: NotRequired[str]
    state_or_province: NotRequired[str]
    street_address: NotRequired[str]
    street_address2: NotRequired[str]
