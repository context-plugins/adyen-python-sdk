
# Total Amount Restriction 1

The total amount and the operation.

Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.

## Structure

`TotalAmountRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The amount value and currency. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.total_amount_restriction_1 import TotalAmountRestriction1

total_amount_restriction_1 = TotalAmountRestriction1(
    operation='operation6',
    value=Amount17(
        currency='currency2',
        value=128
    )
)
```

