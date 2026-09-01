from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .destination1 import Destination1, Destination1Dict
from .item_detail_line import ItemDetailLine, ItemDetailLineDict


class LevelTwoThree2(SdkBaseModel):
    """`Level 2 and Level 3 enhanced scheme data
    <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3/>`__ that may be required for processing
    the transaction and/or for interchange savings."""

    customer_reference_number: Optional[str] = Field(default=UNSET, alias="customerReferenceNumber")
    """The reference number to identify the customer and their order.
    * Format: ASCII
    * Max length: 25 characters
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``enhancedSchemeData.customerReference``"""

    destination: Optional[Destination1] = UNSET
    """The destination address information."""

    duty_amount: Optional[int] = Field(default=UNSET, alias="dutyAmount")
    """The duty tax amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``enhancedSchemeData.dutyAmount``"""

    freight_amount: Optional[int] = Field(default=UNSET, alias="freightAmount")
    """The shipping amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``enhancedSchemeData.freightAmount``"""

    item_detail_lines: Optional[list[ItemDetailLine]] = Field(default=UNSET, alias="itemDetailLines")
    """The list of item detail lines."""

    order_date: Optional[Date] = Field(default=UNSET, alias="orderDate")
    """The date of the order.
    * Min Length: 10 characters
    * Max Length: 10 characters
    * Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: yyyy-MM-dd
    * **additionalData key:** ``enhancedSchemeData.orderDate``"""

    ship_from_postal_code: Optional[str] = Field(default=UNSET, alias="shipFromPostalCode")
    """The postal code of the address where the item is shipped from.
    * Encoding: ASCII
    * Max length: 10 characters
    * For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.
    * For Canada, it must be in 6 digits format. For example, M4B 1G5.
    * **additionalData key:** ``enhancedSchemeData.shipFromPostalCode``"""

    total_tax_amount: Optional[int] = Field(default=UNSET, alias="totalTaxAmount")
    """The amount of state or provincial `tax included in the total transaction amount
    <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3#requirements-to-send-level-2-3-esd>`__, in
    `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * For L2 data: must not be all zeroes.
    * For L3 data: can be zero.
    * **additionalData key:** ``enhancedSchemeData.totalTaxAmount``"""


class LevelTwoThree2Dict(TypedDict):
    customer_reference_number: NotRequired[str]
    destination: NotRequired[Destination1 | Destination1Dict]
    duty_amount: NotRequired[int]
    freight_amount: NotRequired[int]
    item_detail_lines: NotRequired[list[ItemDetailLine | ItemDetailLineDict]]
    order_date: NotRequired[Date]
    ship_from_postal_code: NotRequired[str]
    total_tax_amount: NotRequired[int]
