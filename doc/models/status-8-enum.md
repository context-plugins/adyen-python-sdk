
# Status 8 Enum

The status of the store. Possible values: **Pending**, **Active**, **Inactive**, **InactiveWithModifications**, **Closed**.

## Enumeration

`Status8Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |
| `INACTIVEWITHMODIFICATIONS` |
| `PENDING` |

## Example

```python
from adyen.models.status_8_enum import Status8Enum

status_8 = Status8Enum.INACTIVE
```

