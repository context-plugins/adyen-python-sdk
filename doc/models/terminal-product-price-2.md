
# Terminal Product Price 2

The price of the product.

## Structure

`TerminalProductPrice2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `value` | `float` | Optional | The price of the item. |

## Example

```python
from adyen.models.terminal_product_price_2 import TerminalProductPrice2

terminal_product_price_2 = TerminalProductPrice2(
    currency='currency4',
    value=112.76
)
```

