from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataSubMerchant(SdkBaseModel):
    sub_merchant_number_of_sub_sellers: Optional[str] = Field(default=UNSET, alias="subMerchant.numberOfSubSellers")
    """Required for transactions performed by registered payment facilitators. Indicates the number of sub-merchants
    contained in the request. For example, **3**."""

    sub_merchant_sub_seller_sub_seller_nr_city: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].city"
    )
    """Required for transactions performed by registered payment facilitators. The city of the sub-merchant's address.
    * Format: Alphanumeric
    * Maximum length: 13 characters"""

    sub_merchant_sub_seller_sub_seller_nr_country: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].country"
    )
    """Required for transactions performed by registered payment facilitators. The three-letter country code of the
    sub-merchant's address. For example, **BRA** for Brazil.
    * Format: `ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`__
    * Fixed length: 3 characters"""

    sub_merchant_sub_seller_sub_seller_nr_email: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].email"
    )
    """Required for transactions performed by registered payment facilitators. The email address of the sub-merchant.
    * Format: Alphanumeric
    * Maximum length: 40 characters"""

    sub_merchant_sub_seller_sub_seller_nr_id: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].id"
    )
    """Required for transactions performed by registered payment facilitators. A unique identifier that you create for
    the sub-merchant, used by schemes to identify the sub-merchant.
    * Format: Alphanumeric
    * Maximum length: 15 characters"""

    sub_merchant_sub_seller_sub_seller_nr_mcc: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].mcc"
    )
    """Required for transactions performed by registered payment facilitators. The sub-merchant's 4-digit Merchant
    Category Code (MCC).
    * Format: Numeric
    * Fixed length: 4 digits"""

    sub_merchant_sub_seller_sub_seller_nr_name: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].name"
    )
    """Required for transactions performed by registered payment facilitators. The name of the sub-merchant. Based on
    scheme specifications, this value will overwrite the shopper statement that will appear in the card statement.
    Exception: for acquirers in Brazil, this value does not overwrite the shopper statement.
    * Format: Alphanumeric
    * Maximum length: 22 characters"""

    sub_merchant_sub_seller_sub_seller_nr_phone_number: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].phoneNumber"
    )
    """Required for transactions performed by registered payment facilitators. The phone number of the sub-merchant.
    * Format: Alphanumeric and special characters
    * Maximum length: 20 characters"""

    sub_merchant_sub_seller_sub_seller_nr_postal_code: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].postalCode"
    )
    """Required for transactions performed by registered payment facilitators. The postal code of the sub-merchant's
    address, without dashes.
    * Format: Numeric
    * Fixed length: 8 digits"""

    sub_merchant_sub_seller_sub_seller_nr_state: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].state"
    )
    """Required for transactions performed by registered payment facilitators. The state code of the sub-merchant's
    address, if applicable to the country.
    * Format: Alphanumeric
    * Maximum length: 2 characters"""

    sub_merchant_sub_seller_sub_seller_nr_street: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].street"
    )
    """Required for transactions performed by registered payment facilitators. The street name and house number of the
    sub-merchant's address.
    * Format: Alphanumeric
    * Maximum length: 60 characters"""

    sub_merchant_sub_seller_sub_seller_nr_tax_id: Optional[str] = Field(
        default=UNSET, alias="subMerchant.subSeller[subSellerNr].taxId"
    )
    """Required for transactions performed by registered payment facilitators. The tax ID of the sub-merchant.
    * Format: Numeric
    * Fixed length: 11 digits for the CPF or 14 digits for the CNPJ"""


class AdditionalDataSubMerchantDict(TypedDict):
    sub_merchant_number_of_sub_sellers: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_city: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_country: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_email: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_id: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_mcc: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_name: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_phone_number: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_postal_code: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_state: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_street: NotRequired[str]
    sub_merchant_sub_seller_sub_seller_nr_tax_id: NotRequired[str]
