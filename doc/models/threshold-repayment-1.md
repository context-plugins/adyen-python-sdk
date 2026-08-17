
# Threshold Repayment 1

## Structure

`ThresholdRepayment1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The minimum threshold amount that your user must repay on every 30-day period. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.threshold_repayment_1 import ThresholdRepayment1

threshold_repayment_1 = ThresholdRepayment1(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

