
# Interchange

Deducts the interchange fee from specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.

## Enumeration

`Interchange`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.interchange import Interchange

interchange = Interchange.DEDUCTFROMLIABLEACCOUNT
```

