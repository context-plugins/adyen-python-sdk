
# Type 112 Enum

The type of entity that owns the bank account or card.

Possible values: **individual**, **organization**, or **unknown**.

Required when `category` is **card**. In this case, the value must be **individual**.

## Enumeration

`Type112Enum`

## Fields

| Name |
|  --- |
| `INDIVIDUAL` |
| `ORGANIZATION` |
| `UNKNOWN` |

## Example

```python
from adyen.models.type_112_enum import Type112Enum

type_112 = Type112Enum.UNKNOWN
```

