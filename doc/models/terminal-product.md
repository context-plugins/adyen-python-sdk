
# Terminal Product

*This model accepts additional fields of type Any.*

## Structure

`TerminalProduct`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Information about items included and integration options. |
| `id` | `str` | Optional | The unique identifier of the product. |
| `items_included` | `List[str]` | Optional | A list of parts included in the terminal package. |
| `name` | `str` | Optional | The descriptive name of the product. |
| `price` | [`TerminalProductPrice`](../../doc/models/terminal-product-price.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.terminal_product import TerminalProduct
from adyen.models.terminal_product_price import TerminalProductPrice

terminal_product = TerminalProduct(
    description='description6',
    id='id6',
    items_included=[
        'itemsIncluded9',
        'itemsIncluded0'
    ],
    name='name6',
    price=TerminalProductPrice(
        currency='currency2',
        value=203.04,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

