
# Scheme Fee

Deducts the scheme fee from the specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.

## Enumeration

`SchemeFee`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.scheme_fee import SchemeFee

scheme_fee = SchemeFee.DEDUCTFROMLIABLEACCOUNT
```

