
# Refund Cost Allocation Enum

Deducts the refund costs from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**

## Enumeration

`RefundCostAllocationEnum`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.refund_cost_allocation_enum import RefundCostAllocationEnum

refund_cost_allocation = RefundCostAllocationEnum.DEDUCTFROMLIABLEACCOUNT
```

