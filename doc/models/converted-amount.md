
# Converted Amount

## Structure

`ConvertedAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_value` | `float` | Required | Value of an amount.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `currency` | `str` | Required | Currency of a monetary amount.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |

## Example

```python
from adyen.models.converted_amount import ConvertedAmount

converted_amount = ConvertedAmount(
    amount_value=50.14,
    currency='Currency2'
)
```

