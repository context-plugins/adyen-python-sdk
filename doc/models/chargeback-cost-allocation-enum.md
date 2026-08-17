
# Chargeback Cost Allocation Enum

Deducts the chargeback costs from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**

## Enumeration

`ChargebackCostAllocationEnum`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.chargeback_cost_allocation_enum import ChargebackCostAllocationEnum

chargeback_cost_allocation = ChargebackCostAllocationEnum.DEDUCTFROMLIABLEACCOUNT
```

