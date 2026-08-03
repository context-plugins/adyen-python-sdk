
# Chargeback Cost Allocation

Deducts the chargeback costs from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**

## Enumeration

`ChargebackCostAllocation`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.chargeback_cost_allocation import ChargebackCostAllocation

chargeback_cost_allocation = ChargebackCostAllocation.DEDUCTFROMLIABLEACCOUNT
```

