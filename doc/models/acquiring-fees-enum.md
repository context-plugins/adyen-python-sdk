
# Acquiring Fees Enum

Deducts the acquiring fees (the aggregated amount of interchange and scheme fee) from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.

## Enumeration

`AcquiringFeesEnum`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.acquiring_fees_enum import AcquiringFeesEnum

acquiring_fees = AcquiringFeesEnum.DEDUCTFROMLIABLEACCOUNT
```

