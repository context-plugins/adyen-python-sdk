
# Terminal Product

## Structure

`TerminalProduct`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Information about items included and integration options. |
| `id` | `str` | Optional | The unique identifier of the product. |
| `items_included` | `List[str]` | Optional | A list of parts included in the terminal package. |
| `name` | `str` | Optional | The descriptive name of the product. |
| `price` | [`TerminalProductPrice2`](../../doc/models/terminal-product-price-2.md) | Optional | The price of the product. |

## Example

```python
from adyen.models.terminal_product import TerminalProduct
from adyen.models.terminal_product_price_2 import TerminalProductPrice2

terminal_product = TerminalProduct(
    description='description6',
    id='id6',
    items_included=[
        'itemsIncluded9',
        'itemsIncluded0'
    ],
    name='name6',
    price=TerminalProductPrice2(
        currency='currency2',
        value=203.04
    )
)
```

