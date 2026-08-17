
# Threshold Repayment

## Structure

`ThresholdRepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The amount to be repaid on a 30-day basis. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.threshold_repayment import ThresholdRepayment

threshold_repayment = ThresholdRepayment(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

