
# Surcharge 3 Enum

Books the surcharge amount to the specified balance account.

Possible values: **addToLiableAccount**, **addToOneBalanceAccount**

## Enumeration

`Surcharge3Enum`

## Fields

| Name |
|  --- |
| `ADDTOLIABLEACCOUNT` |
| `ADDTOONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.surcharge_3_enum import Surcharge3Enum

surcharge_3 = Surcharge3Enum.ADDTOLIABLEACCOUNT
```

