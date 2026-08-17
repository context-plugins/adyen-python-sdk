
# Status 23 Enum

The status of the balance account, set to **active** by default.

## Enumeration

`Status23Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |
| `SUSPENDED` |

## Example

```python
from adyen.models.status_23_enum import Status23Enum

status_23 = Status23Enum.INACTIVE
```

