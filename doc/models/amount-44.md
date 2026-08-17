
# Amount 44

The updated final payment amount. This amount is the item total plus the shipping costs of the selected `deliveryMethod`.

## Structure

`Amount44`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `value` | `int` | Required | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |

## Example

```python
from adyen.models.amount_44 import Amount44

amount_44 = Amount44(
    currency='currency4',
    value=2
)
```

