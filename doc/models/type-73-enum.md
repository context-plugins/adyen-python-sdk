
# Type 73 Enum

The type of the transfer event. Possible values: **accounting**, **tracking**.

## Enumeration

`Type73Enum`

## Fields

| Name |
|  --- |
| `ACCOUNTING` |
| `TRACING` |
| `TRACKING` |

## Example

```python
from adyen.models.type_73_enum import Type73Enum

type_73 = Type73Enum.ACCOUNTING
```

