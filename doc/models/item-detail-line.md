
# Item Detail Line

*This model accepts additional fields of type Any.*

## Structure

`ItemDetailLine`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `commodity_code` | `str` | Optional | The code that identifies the item in a standardized commodity coding scheme. There are different commodity coding schemes:<br><br>* [UNSPSC commodity codes](https://www.ungm.org/public/unspsc)<br><br>* [HS commodity codes](https://www.wcoomd.org/en/topics/nomenclature/overview.aspx)<br><br>* [NAICS commodity codes](https://www.census.gov/naics/)<br><br>* [NAPCS commodity codes](https://www.census.gov/naics/napcs/)<br><br>* Encoding: ASCII<br><br>* Max length: 12 characters<br><br>* Must not start with a space or be all spaces.<br><br>* Must not be all zeros.<br><br>* **additionalData key:** `enhancedSchemeData.itemDetailLine[N].commodityCode` |
| `description` | `str` | Optional | A description of the item, that provides details about the purchase.<br><br>For Visa transactions with level 3 ESD, the description must not be the same or very similar to your merchant name, or, consist only of common words like "product", or "service".<br><br>* Encoding: ASCII<br>* Max length: 26 characters<br>* Must not be a single character.<br>* Must not be blank.<br>* Must not be all special characters.<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `enhancedSchemeData.itemDetailLine[N].description` |
| `discount_amount` | `int` | Optional | The discount amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `enhancedSchemeData.itemDetailLine[N].discountAmount` |
| `product_code` | `str` | Optional | The product code. Must be a unique product code associated with the item or service. This can be your unique code for the item, or the manufacturer's product code.<br><br>* Encoding: ASCII.<br>* Max length: 12 characters<br>* **additionalData key:** `enhancedSchemeData.itemDetailLine[N].productCode` |
| `quantity` | `int` | Optional | The number of items. Must be an integer greater than zero.<br><br>* Encoding: Numeric<br>* Max value: 9999<br>* **additionalData key:** `enhancedSchemeData.itemDetailLine[N].quantity` |
| `total_amount` | `int` | Optional | The total amount for the line item, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br><br>See [Amount requirements for level 2/3 ESD](https://docs.adyen.com//payment-methods/cards/enhanced-scheme-data/l2-l3#amount-requirements) to learn more about how to calculate the line item total.<br><br>* **additionalData key:** `enhancedSchemeData.itemDetailLine[N].totalAmount` |
| `unit_of_measure` | `str` | Optional | The unit of measurement for an item.<br><br>* Encoding: ASCII<br>* Max length: 3 characters<br>* **additionalData key:** `enhancedSchemeData.itemDetailLine[N].unitOfMeasure` |
| `unit_price` | `int` | Optional | The unit price, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `enhancedSchemeData.itemDetailLine[N].unitPrice` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.item_detail_line import ItemDetailLine

item_detail_line = ItemDetailLine(
    commodity_code='commodityCode2',
    description='description6',
    discount_amount=106,
    product_code='productCode8',
    quantity=70,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

