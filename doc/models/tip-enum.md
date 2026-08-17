
# Tip Enum

Books the tips (gratuity) to the specified balance account.

Possible values: **addToLiableAccount**, **addToOneBalanceAccount**.

## Enumeration

`TipEnum`

## Fields

| Name |
|  --- |
| `ADDTOLIABLEACCOUNT` |
| `ADDTOONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.tip_enum import TipEnum

tip = TipEnum.ADDTOLIABLEACCOUNT
```

