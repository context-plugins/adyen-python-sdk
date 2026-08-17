
# Amount 34

An object specifying the currency and value to which you want to convert the source amount (the target amount).

## Structure

`Amount34`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes). |
| `value` | `int` | Required | The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |

## Example

```python
from adyen.models.amount_34 import Amount34

amount_34 = Amount34(
    currency='currency2',
    value=248
)
```

