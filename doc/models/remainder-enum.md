
# Remainder Enum

Books the amount left over after currency conversion to the specified balance account.

Possible values: **addToLiableAccount**, **addToOneBalanceAccount**.

## Enumeration

`RemainderEnum`

## Fields

| Name |
|  --- |
| `ADDTOLIABLEACCOUNT` |
| `ADDTOONEBALANCEACCOUNT` |

## Example

```python
from adyen.models.remainder_enum import RemainderEnum

remainder = RemainderEnum.ADDTOLIABLEACCOUNT
```

