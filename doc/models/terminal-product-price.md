
# Terminal Product Price

## Structure

`TerminalProductPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `value` | `float` | Optional | The price of the item. |

## Example

```python
from adyen.models.terminal_product_price import TerminalProductPrice

terminal_product_price = TerminalProductPrice(
    currency='currency0',
    value=30.82
)
```

