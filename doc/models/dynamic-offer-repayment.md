
# Dynamic Offer Repayment

## Structure

`DynamicOfferRepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `term` | [`RepaymentTerm`](../../doc/models/repayment-term.md) | Required | Contains information about the time period in which your user must repay the total amount of the grant. |

## Example

```python
from adyen.models.dynamic_offer_repayment import DynamicOfferRepayment
from adyen.models.repayment_term import RepaymentTerm

dynamic_offer_repayment = DynamicOfferRepayment(
    term=RepaymentTerm(
        estimated_days=248,
        maximum_days=24
    )
)
```

