
# Status 71 Enum

The status of the PIN delivery.

## Enumeration

`Status71Enum`

## Fields

| Name |
|  --- |
| `CREATED` |
| `DELIVERED` |
| `NOTAPPLICABLE` |
| `PROCESSING` |
| `PRODUCED` |
| `REJECTED` |
| `SHIPPED` |
| `UNKNOWN` |

## Example

```python
from adyen.models.status_71_enum import Status71Enum

status_71 = Status71Enum.SHIPPED
```

