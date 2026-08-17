
# Repayment 2

Details of the repayment configuration.

## Structure

`Repayment2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `basis_points` | `int` | Required | The repayment that is deducted daily from incoming net volume, in [basis points](https://www.investopedia.com/terms/b/basispoint.asp). |
| `term` | [`RepaymentTerm`](../../doc/models/repayment-term.md) | Optional | An object containing the details of the configuration for repayment term. |
| `threshold` | [`ThresholdRepayment2`](../../doc/models/threshold-repayment-2.md) | Optional | An object containing the details of the 30-day repayment threshold. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.repayment_2 import Repayment2
from adyen.models.repayment_term import RepaymentTerm
from adyen.models.threshold_repayment_2 import ThresholdRepayment2

repayment_2 = Repayment2(
    basis_points=86,
    term=RepaymentTerm(
        estimated_days=248,
        maximum_days=24
    ),
    threshold=ThresholdRepayment2(
        amount=Amount17(
            currency='currency2',
            value=110
        )
    )
)
```

