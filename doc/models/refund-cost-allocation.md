
# Refund Cost Allocation

Deducts the refund costs from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**

## Enumeration

`RefundCostAllocation`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.refund_cost_allocation import RefundCostAllocation

refund_cost_allocation = RefundCostAllocation.DEDUCTFROMLIABLEACCOUNT
```

