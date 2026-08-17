
# Amount 22

The currency of the amount you converted (the source amount).

## Structure

`Amount22`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes). |
| `value` | `int` | Required | The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |

## Example

```python
from adyen.models.amount_22 import Amount22

amount_22 = Amount22(
    currency='currency6',
    value=110
)
```

