
# Type 213 Enum

The type of legal entity.

Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**.

## Enumeration

`Type213Enum`

## Fields

| Name |
|  --- |
| `INDIVIDUAL` |
| `ORGANIZATION` |
| `SOLEPROPRIETORSHIP` |
| `TRUST` |
| `UNINCORPORATEDPARTNERSHIP` |

## Example

```python
from adyen.models.type_213_enum import Type213Enum

type_213 = Type213Enum.TRUST
```

