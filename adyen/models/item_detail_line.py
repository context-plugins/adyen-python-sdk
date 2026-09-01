from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemDetailLine(SdkBaseModel):
    commodity_code: Optional[str] = Field(default=UNSET, alias="commodityCode")
    """The code that identifies the item in a standardized commodity coding scheme. There are different commodity coding
    schemes:
    * `UNSPSC commodity codes <https://www.ungm.org/public/unspsc>`__
    * `HS commodity codes <https://www.wcoomd.org/en/topics/nomenclature/overview.aspx>`__
    * `NAICS commodity codes <https://www.census.gov/naics/>`__
    * `NAPCS commodity codes <https://www.census.gov/naics/napcs/>`__


    * Encoding: ASCII
    * Max length: 12 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``enhancedSchemeData.itemDetailLine[N].commodityCode``"""

    description: Optional[str] = UNSET
    """A description of the item, that provides details about the purchase.

     For Visa transactions with level 3 ESD, the description must not be the same or very similar to your merchant name,
        or, consist only of common words like "product", or "service".
    * Encoding: ASCII
    * Max length: 26 characters
    * Must not be a single character.
    * Must not be blank.
    * Must not be all special characters.
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``enhancedSchemeData.itemDetailLine[N].description``"""

    discount_amount: Optional[int] = Field(default=UNSET, alias="discountAmount")
    """The discount amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``enhancedSchemeData.itemDetailLine[N].discountAmount``"""

    product_code: Optional[str] = Field(default=UNSET, alias="productCode")
    """The product code. Must be a unique product code associated with the item or service. This can be your unique code
    for the item, or the manufacturer's product code.
    * Encoding: ASCII.
    * Max length: 12 characters
    * **additionalData key:** ``enhancedSchemeData.itemDetailLine[N].productCode``"""

    quantity: Optional[int] = UNSET
    """The number of items. Must be an integer greater than zero.
    * Encoding: Numeric
    * Max value: 9999
    * **additionalData key:** ``enhancedSchemeData.itemDetailLine[N].quantity``"""

    total_amount: Optional[int] = Field(default=UNSET, alias="totalAmount")
    """The total amount for the line item, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000

    See `Amount requirements for level 2/3 ESD
    <https://docs.adyen.com//payment-methods/cards/enhanced-scheme-data/l2-l3#amount-requirements>`__ to learn more
    about how to calculate the line item total.
    * **additionalData key:** ``enhancedSchemeData.itemDetailLine[N].totalAmount``"""

    unit_of_measure: Optional[str] = Field(default=UNSET, alias="unitOfMeasure")
    """The unit of measurement for an item.
    * Encoding: ASCII
    * Max length: 3 characters
    * **additionalData key:** ``enhancedSchemeData.itemDetailLine[N].unitOfMeasure``"""

    unit_price: Optional[int] = Field(default=UNSET, alias="unitPrice")
    """The unit price, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``enhancedSchemeData.itemDetailLine[N].unitPrice``"""


class ItemDetailLineDict(TypedDict):
    commodity_code: NotRequired[str]
    description: NotRequired[str]
    discount_amount: NotRequired[int]
    product_code: NotRequired[str]
    quantity: NotRequired[int]
    total_amount: NotRequired[int]
    unit_of_measure: NotRequired[str]
    unit_price: NotRequired[int]
