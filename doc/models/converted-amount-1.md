
# Converted Amount 1

Amount after a currency conversion.

## Structure

`ConvertedAmount1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_value` | `float` | Required | Value of an amount.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `currency` | `str` | Required | Currency of a monetary amount.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |

## Example

```python
from adyen.models.converted_amount_1 import ConvertedAmount1

converted_amount_1 = ConvertedAmount1(
    amount_value=184.32,
    currency='Currency0'
)
```

