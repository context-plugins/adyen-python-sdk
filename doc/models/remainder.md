
# Remainder

Books the amount left over after currency conversion to the specified balance account.

Possible values: **addToLiableAccount**, **addToOneBalanceAccount**.

## Enumeration

`Remainder`

## Fields

| Name |
|  --- |
| `ADDTOLIABLEACCOUNT` |
| `ADDTOONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.remainder import Remainder

remainder = Remainder.ADDTOLIABLEACCOUNT
```

