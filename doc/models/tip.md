
# Tip

Books the tips (gratuity) to the specified balance account.

Possible values: **addToLiableAccount**, **addToOneBalanceAccount**.

## Enumeration

`Tip`

## Fields

| Name |
|  --- |
| `ADDTOLIABLEACCOUNT` |
| `ADDTOONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.tip import Tip

tip = Tip.ADDTOLIABLEACCOUNT
```

