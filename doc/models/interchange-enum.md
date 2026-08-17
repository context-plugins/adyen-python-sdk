
# Interchange Enum

Deducts the interchange fee from specified balance account.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**.

## Enumeration

`InterchangeEnum`

## Fields

| Name |
|  --- |
| `DEDUCTFROMLIABLEACCOUNT` |
| `DEDUCTFROMONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.interchange_enum import InterchangeEnum

interchange = InterchangeEnum.DEDUCTFROMLIABLEACCOUNT
```

