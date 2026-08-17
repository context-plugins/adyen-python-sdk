
# Amount 7

For prepaid or gift card purchase, the purchase amount total of prepaid or gift card(s).

## Structure

`Amount7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `value` | `int` | Required | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |

## Example

```python
from adyen.models.amount_7 import Amount7

amount_7 = Amount7(
    currency='currency8',
    value=18
)
```

