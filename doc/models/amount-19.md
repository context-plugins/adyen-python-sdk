
# Amount 19

An object specifying the currency and value for which you want to perform an exchange calculation.

## Structure

`Amount19`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes). |
| `value` | `int` | Required | The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |

## Example

```python
from adyen.models.amount_19 import Amount19

amount_19 = Amount19(
    currency='currency2',
    value=222
)
```

