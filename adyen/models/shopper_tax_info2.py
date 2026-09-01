from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShopperTaxInfo2(SdkBaseModel):
    """The tax info of the shopper"""

    tax_country_code: str = Field(alias="taxCountryCode")
    """The two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code
    associated with the provided tax identification number. Currently used only for Indian PA-CB tax verification, when
    applicable."""

    tax_identification_number: str = Field(alias="taxIdentificationNumber")
    """The shopper’s tax identification number."""


class ShopperTaxInfo2Dict(TypedDict):
    tax_country_code: str
    tax_identification_number: str
