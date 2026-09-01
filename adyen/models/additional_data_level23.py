from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataLevel23(SdkBaseModel):
    enhanced_scheme_data_customer_reference: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.customerReference"
    )
    """The reference number to identify the customer and their order.
    * Encoding: ASCII
    * Max length: 25 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros."""

    enhanced_scheme_data_destination_country_code: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.destinationCountryCode"
    )
    """The three-letter `ISO 3166-1 alpha-3 country code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`__ for the
    destination address.
    * Encoding: ASCII
    * Fixed length: 3 characters"""

    enhanced_scheme_data_destination_postal_code: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.destinationPostalCode"
    )
    """The postal code of the destination address.
    * Encoding: ASCII
    * Max length: 10 characters
    * Must not start with a space.
    * For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.
    * For Canada, it must be in 6 digits format. For example, M4B 1G5."""

    enhanced_scheme_data_destination_state_province_code: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.destinationStateProvinceCode"
    )
    """The state or province code of the destination address.
    * Encoding: ASCII
    * Max length: 3 characters
    * Must not start with a space."""

    enhanced_scheme_data_duty_amount: Optional[str] = Field(default=UNSET, alias="enhancedSchemeData.dutyAmount")
    """The duty tax amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max length: 12 characters"""

    enhanced_scheme_data_freight_amount: Optional[str] = Field(default=UNSET, alias="enhancedSchemeData.freightAmount")
    """The shipping amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max length: 12 characters"""

    enhanced_scheme_data_item_detail_line_item_nr_commodity_code: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.itemDetailLine[itemNr].commodityCode"
    )
    """The code that identifies the item in a standardized commodity coding scheme. There are different commodity coding
    schemes:
    * `UNSPSC commodity codes <https://www.ungm.org/public/unspsc>`__
    * `HS commodity codes <https://www.wcoomd.org/en/topics/nomenclature/overview.aspx>`__
    * `NAICS commodity codes <https://www.census.gov/naics/>`__
    * `NAPCS commodity codes <https://www.census.gov/naics/napcs/>`__


    * Encoding: ASCII
    * Max length: 12 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros."""

    enhanced_scheme_data_item_detail_line_item_nr_description: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.itemDetailLine[itemNr].description"
    )
    """A description of the item, that provides details about the purchase.

     For Visa transactions with level 3 ESD, the description must not be the same or very similar to your merchant name,
        or, consist only of common words like "product", or "service".
    * Encoding: ASCII
    * Max length: 26 characters
    * Must not be a single character.
    * Must not be blank.
    * Must not be all special characters.
    * Must not be blank.
    * Must not start with a space or be all spaces.
    * Must not be all zeros."""

    enhanced_scheme_data_item_detail_line_item_nr_discount_amount: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.itemDetailLine[itemNr].discountAmount"
    )
    """The discount amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max length: 12 characters"""

    enhanced_scheme_data_item_detail_line_item_nr_product_code: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.itemDetailLine[itemNr].productCode"
    )
    """The product code. Must be a unique product code associated with the item or service. This can be your unique code
    for the item, or the manufacturer's product code.
    * Encoding: ASCII.
    * Max length: 12 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros."""

    enhanced_scheme_data_item_detail_line_item_nr_quantity: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.itemDetailLine[itemNr].quantity"
    )
    """The number of items. Must be an integer greater than zero.
    * Encoding: Numeric
    * Max length: 12 characters
    * Must not start with a space or be all spaces."""

    enhanced_scheme_data_item_detail_line_item_nr_total_amount: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.itemDetailLine[itemNr].totalAmount"
    )
    """The total amount for the line item, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__. See `Amount requirements for level 2/3 ESD
    <https://docs.adyen.com//payment-methods/cards/enhanced-scheme-data/l2-l3#amount-requirements>`__ to learn more
    about how to calculate the line item total.
    * For example, 2000 means USD 20.00.
    * Max length: 12 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros."""

    enhanced_scheme_data_item_detail_line_item_nr_unit_of_measure: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.itemDetailLine[itemNr].unitOfMeasure"
    )
    """The unit of measurement for an item.
    * Encoding: ASCII
    * Max length: 3 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros."""

    enhanced_scheme_data_item_detail_line_item_nr_unit_price: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.itemDetailLine[itemNr].unitPrice"
    )
    """The unit price in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max length: 12 characters
    * Must not be all zeros."""

    enhanced_scheme_data_order_date: Optional[str] = Field(default=UNSET, alias="enhancedSchemeData.orderDate")
    """The order date.
    * Format: ``ddMMyy``
    * Encoding: ASCII
    * Max length: 6 characters"""

    enhanced_scheme_data_ship_from_postal_code: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.shipFromPostalCode"
    )
    """The postal code of the address where the item is shipped from.
    * Encoding: ASCII
    * Max length: 10 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.
    * For Canada, it must be in 6 digits format. For example, M4B 1G5."""

    enhanced_scheme_data_total_tax_amount: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.totalTaxAmount"
    )
    """The amount of state or provincial `tax included in the total transaction amount
    <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3#requirements-to-send-level-2-3-esd>`__, in
    `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max length: 12 characters
    * For L2 data: must not be all zeroes.
    * For L3 data: can be zero."""


class AdditionalDataLevel23Dict(TypedDict):
    enhanced_scheme_data_customer_reference: NotRequired[str]
    enhanced_scheme_data_destination_country_code: NotRequired[str]
    enhanced_scheme_data_destination_postal_code: NotRequired[str]
    enhanced_scheme_data_destination_state_province_code: NotRequired[str]
    enhanced_scheme_data_duty_amount: NotRequired[str]
    enhanced_scheme_data_freight_amount: NotRequired[str]
    enhanced_scheme_data_item_detail_line_item_nr_commodity_code: NotRequired[str]
    enhanced_scheme_data_item_detail_line_item_nr_description: NotRequired[str]
    enhanced_scheme_data_item_detail_line_item_nr_discount_amount: NotRequired[str]
    enhanced_scheme_data_item_detail_line_item_nr_product_code: NotRequired[str]
    enhanced_scheme_data_item_detail_line_item_nr_quantity: NotRequired[str]
    enhanced_scheme_data_item_detail_line_item_nr_total_amount: NotRequired[str]
    enhanced_scheme_data_item_detail_line_item_nr_unit_of_measure: NotRequired[str]
    enhanced_scheme_data_item_detail_line_item_nr_unit_price: NotRequired[str]
    enhanced_scheme_data_order_date: NotRequired[str]
    enhanced_scheme_data_ship_from_postal_code: NotRequired[str]
    enhanced_scheme_data_total_tax_amount: NotRequired[str]
