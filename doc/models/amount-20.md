
# Amount 20

## Structure

`Amount20`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO 4217 currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes).<br><br>**Constraints**: *Minimum Length*: `1` |
| `value` | `int` | Required | The amount of the transaction in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units) (cents). |

## Example

```python
from adyen.models.amount_20 import Amount20

amount_20 = Amount20(
    currency='EUR',
    value=499
)
```

