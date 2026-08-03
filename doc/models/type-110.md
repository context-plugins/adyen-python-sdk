
# Type 110

The type of entity that owns the bank account or card.

Possible values: **individual**, **organization**, or **unknown**.

Required when `category` is **card**. In this case, the value must be **individual**.

## Enumeration

`Type110`

## Fields

| Name |
|  --- |
| `INDIVIDUAL` |
| `ORGANIZATION` |
| `UNKNOWN` |

## Example

```python
from adyen.models.type_110 import Type110

type_110 = Type110.ORGANIZATION
```

