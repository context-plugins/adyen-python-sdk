
# Terminal Product Price 2

The price of the product.

*This model accepts additional fields of type Any.*

## Structure

`TerminalProductPrice2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `value` | `float` | Optional | The price of the item. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.terminal_product_price_2 import TerminalProductPrice2

terminal_product_price_2 = TerminalProductPrice2(
    currency='currency4',
    value=112.76,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

