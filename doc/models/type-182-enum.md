
# Type 182 Enum

The type of legal entity.

Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**.

## Enumeration

`Type182Enum`

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
from adyen.models.type_182_enum import Type182Enum

type_182 = Type182Enum.UNINCORPORATEDPARTNERSHIP
```

