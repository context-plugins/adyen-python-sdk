
# Type 182

The type of legal entity.

Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**.

## Enumeration

`Type182`

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
from adyen.models.type_182 import Type182

type_182 = Type182.UNINCORPORATEDPARTNERSHIP
```

