
# Type 111 Enum

The type of payment instrument.

Possible values: **card**, **bankAccount**.

## Enumeration

`Type111Enum`

## Fields

| Name |
|  --- |
| `BANKACCOUNT` |
| `CARD` |

## Example

```python
from adyen.models.type_111_enum import Type111Enum

type_111 = Type111Enum.BANKACCOUNT
```

