
# Level Two Three 2

[Level 2 and Level 3 enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3/) that may be required for processing the transaction and/or for interchange savings.

## Structure

`LevelTwoThree2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_reference_number` | `str` | Optional | The reference number to identify the customer and their order.<br><br>* Format: ASCII<br>* Max length: 25 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `enhancedSchemeData.customerReference` |
| `destination` | [`Destination1`](../../doc/models/destination-1.md) | Optional | The destination address information. |
| `duty_amount` | `int` | Optional | The duty tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `enhancedSchemeData.dutyAmount` |
| `freight_amount` | `int` | Optional | The shipping amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `enhancedSchemeData.freightAmount` |
| `item_detail_lines` | [`List[ItemDetailLine]`](../../doc/models/item-detail-line.md) | Optional | The list of item detail lines. |
| `order_date` | `date` | Optional | The date of the order.<br><br>* Min Length: 10 characters<br>* Max Length: 10 characters<br>* Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd<br>* **additionalData key:** `enhancedSchemeData.orderDate` |
| `ship_from_postal_code` | `str` | Optional | The postal code of the address where the item is shipped from.<br><br>* Encoding: ASCII<br>* Max length: 10 characters<br>* For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.<br>* For Canada, it must be in 6 digits format. For example, M4B 1G5.<br>* **additionalData key:** `enhancedSchemeData.shipFromPostalCode` |
| `total_tax_amount` | `int` | Optional | The amount of state or provincial [tax included in the total transaction amount](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3#requirements-to-send-level-2-3-esd), in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* For L2 data: must not be all zeroes.<br>* For L3 data: can be zero.<br>* **additionalData key:** `enhancedSchemeData.totalTaxAmount` |

## Example

```python
from adyen.models.destination_1 import Destination1
from adyen.models.item_detail_line import ItemDetailLine
from adyen.models.level_two_three_2 import LevelTwoThree2

level_two_three_2 = LevelTwoThree2(
    customer_reference_number='customerReferenceNumber0',
    destination=Destination1(
        country_code='countryCode0',
        postal_code='postalCode6',
        state_or_province='stateOrProvince2'
    ),
    duty_amount=150,
    freight_amount=220,
    item_detail_lines=[
        ItemDetailLine(
            commodity_code='commodityCode4',
            description='description8',
            discount_amount=220,
            product_code='productCode0',
            quantity=184
        )
    ]
)
```

