
# Dynamic Offer Repayment 2

Contains information about the repayment configuration of the grant.

## Structure

`DynamicOfferRepayment2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `term` | [`RepaymentTerm`](../../doc/models/repayment-term.md) | Required | Contains information about the time period in which your user must repay the total amount of the grant. |

## Example

```python
from adyen.models.dynamic_offer_repayment_2 import DynamicOfferRepayment2
from adyen.models.repayment_term import RepaymentTerm

dynamic_offer_repayment_2 = DynamicOfferRepayment2(
    term=RepaymentTerm(
        estimated_days=248,
        maximum_days=24
    )
)
```

