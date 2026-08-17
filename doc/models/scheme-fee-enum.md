
# Scheme Fee Enum

Deducts the scheme fee from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.

## Enumeration

`SchemeFeeEnum`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.scheme_fee_enum import SchemeFeeEnum

scheme_fee = SchemeFeeEnum.DEDUCTFROMLIABLEACCOUNT
```

