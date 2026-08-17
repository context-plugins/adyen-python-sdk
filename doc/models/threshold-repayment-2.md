
# Threshold Repayment 2

An object containing the details of the 30-day repayment threshold.

## Structure

`ThresholdRepayment2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The amount to be repaid on a 30-day basis. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.threshold_repayment_2 import ThresholdRepayment2

threshold_repayment_2 = ThresholdRepayment2(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

