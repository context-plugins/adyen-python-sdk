
# Total Amount Restriction

## Structure

`TotalAmountRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The amount value and currency. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.total_amount_restriction import TotalAmountRestriction

total_amount_restriction = TotalAmountRestriction(
    operation='operation0',
    value=Amount17(
        currency='currency2',
        value=128
    )
)
```

