
# Amount Adjustment

## Structure

`AmountAdjustment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The adjustment amount. |
| `amount_adjustment_type` | [`AmountAdjustmentTypeEnum`](../../doc/models/amount-adjustment-type-enum.md) | Optional | The type of markup that is applied to an authorised payment.<br><br>Possible values: **exchange**, **forexMarkup**, **authHoldReserve**, **atmMarkup**. |
| `basepoints` | `int` | Optional | The basepoints associated with the applied markup. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.amount_adjustment import AmountAdjustment
from adyen.models.amount_adjustment_type_enum import AmountAdjustmentTypeEnum

amount_adjustment = AmountAdjustment(
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    amount_adjustment_type=AmountAdjustmentTypeEnum.ATMMARKUP,
    basepoints=162
)
```

