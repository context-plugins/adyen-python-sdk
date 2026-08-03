
# Amount Adjustment Type

The type of markup that is applied to an authorised payment.

Possible values: **exchange**, **forexMarkup**, **authHoldReserve**, **atmMarkup**.

## Enumeration

`AmountAdjustmentType`

## Fields

| Name |
|  --- |
| `ATMMARKUP` |
| `AUTHHOLDRESERVE` |
| `EXCHANGE` |
| `FOREXMARKUP` |

## Example

```python
from adyen.models.amount_adjustment_type import AmountAdjustmentType

amount_adjustment_type = AmountAdjustmentType.EXCHANGE
```

