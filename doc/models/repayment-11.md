
# Repayment 11

Contains information about the repayment configuration of the grant.

## Structure

`Repayment11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `basis_points` | `int` | Required | The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp). |
| `term` | [`RepaymentTerm`](../../doc/models/repayment-term.md) | Optional | Contains information about the time period in which your user must repay the total amount of the grant. |
| `threshold` | [`ThresholdRepayment21`](../../doc/models/threshold-repayment-21.md) | Optional | Contains the minimum threshold amount that your user must repay every 30-day period. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.repayment_11 import Repayment11
from adyen.models.repayment_term import RepaymentTerm
from adyen.models.threshold_repayment_21 import ThresholdRepayment21

repayment_11 = Repayment11(
    basis_points=94,
    term=RepaymentTerm(
        estimated_days=248,
        maximum_days=24
    ),
    threshold=ThresholdRepayment21(
        amount=Amount17(
            currency='currency2',
            value=110
        )
    )
)
```

