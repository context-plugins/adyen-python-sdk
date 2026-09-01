from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubMerchant(SdkBaseModel):
    """Required for Back-to-Back/ purchase driven load in Wallet transactions. Contains the final merchant who will be
    receiving the money, also known as subMerchant, information."""

    city: Optional[str] = UNSET
    """The city of the sub-merchant's address.
    * Format: Alphanumeric
    * Maximum length: 13 characters"""

    country: Optional[str] = UNSET
    """The three-letter country code of the sub-merchant's address. For example, **BRA** for Brazil.
    * Format: `ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`__
    * Fixed length: 3 characters"""

    mcc: Optional[str] = UNSET
    """The sub-merchant's 4-digit Merchant Category Code (MCC).
    * Format: Numeric
    * Fixed length: 4 digits"""

    name: Optional[str] = UNSET
    """The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement
    that will appear in the card statement.
    * Format: Alphanumeric
    * Maximum length: 22 characters"""

    tax_id: Optional[str] = Field(default=UNSET, alias="taxId")
    """The tax ID of the sub-merchant.
    * Format: Numeric
    * Fixed length: 11 digits for the CPF or 14 digits for the CNPJ"""


class SubMerchantDict(TypedDict):
    city: NotRequired[str]
    country: NotRequired[str]
    mcc: NotRequired[str]
    name: NotRequired[str]
    tax_id: NotRequired[str]
