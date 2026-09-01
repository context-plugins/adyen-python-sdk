from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubMerchantData2(SdkBaseModel):
    city: Optional[str] = UNSET
    """The city of the sub-merchant's address."""

    country: Optional[str] = UNSET
    """The country/region of the sub-merchant's address, specified as the three-letter country code in `ISO 3166-1
    alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`__ format."""

    display_name: str = Field(alias="displayName")
    """The name of the sub-merchant as it should appear on the display of the mobile device during transactions."""

    email: Optional[str] = UNSET
    """The email address of the sub-merchant. Required for American Express."""

    id: str
    """Your unique identifier of the sub-merchant."""

    mcc: str
    """The sub-merchant's four-digit Merchant Category Code (MCC). This parameter is used to correctly route the
    transaction."""

    name: str
    """The name of the sub-merchant."""

    phone_number: Optional[str] = Field(default=UNSET, alias="phoneNumber")
    """The phone number of the sub-merchant. Required for American Express."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The postal code of the sub-merchant's address, without dashes."""

    state: Optional[str] = UNSET
    """The state code of the sub-merchant's address, if applicable for the country or region."""

    street: Optional[str] = UNSET
    """The street name and house number of the sub-merchant's address."""

    tax_id: Optional[str] = Field(default=UNSET, alias="taxId")
    """The tax ID of the sub-merchant. Required only in Brazil and for Cartes Bancaires in France. For Brazil, this is
    the 11-digit CPF or 14-digit CNPJ. For France, this is the SIRET, with a maximum of 14 digits."""


class SubMerchantData2Dict(TypedDict):
    city: NotRequired[str]
    country: NotRequired[str]
    display_name: str
    email: NotRequired[str]
    id: str
    mcc: str
    name: str
    phone_number: NotRequired[str]
    postal_code: NotRequired[str]
    state: NotRequired[str]
    street: NotRequired[str]
    tax_id: NotRequired[str]
