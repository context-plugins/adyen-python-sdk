
# Acquiring Fees

Deducts the acquiring fees (the aggregated amount of interchange and scheme fee) from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.

## Enumeration

`AcquiringFees`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.acquiring_fees import AcquiringFees

acquiring_fees = AcquiringFees.DEDUCTFROMLIABLEACCOUNT
```

