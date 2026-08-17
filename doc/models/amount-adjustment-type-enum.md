
# Amount Adjustment Type Enum

The type of markup that is applied to an authorised payment.

Possible values: **exchange**, **forexMarkup**, **authHoldReserve**, **atmMarkup**.

## Enumeration

`AmountAdjustmentTypeEnum`

## Fields

| Name |
|  --- |
| `ATMMARKUP` |
| `AUTHHOLDRESERVE` |
| `EXCHANGE` |
| `FOREXMARKUP` |

## Example

```python
from adyen.models.amount_adjustment_type_enum import AmountAdjustmentTypeEnum

amount_adjustment_type = AmountAdjustmentTypeEnum.EXCHANGE
```

