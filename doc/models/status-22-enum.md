
# Status 22 Enum

The new status of the account.

> Permitted values: `Active`, `Inactive`, `Suspended`, `Closed`.

## Enumeration

`Status22Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |
| `SUSPENDED` |

## Example

```python
from adyen.models.status_22_enum import Status22Enum

status_22 = Status22Enum.INACTIVE
```

