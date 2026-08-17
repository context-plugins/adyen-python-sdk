
# Threshold Repayment 21

Contains the minimum threshold amount that your user must repay every 30-day period.

## Structure

`ThresholdRepayment21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The minimum threshold amount that your user must repay on every 30-day period. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.threshold_repayment_21 import ThresholdRepayment21

threshold_repayment_21 = ThresholdRepayment21(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

