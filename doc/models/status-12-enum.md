
# Status 12 Enum

The status of the account holder.

> Permitted values: `Active`, `Inactive`, `Suspended`, `Closed`.

## Enumeration

`Status12Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |
| `SUSPENDED` |

## Example

```python
from adyen.models.status_12_enum import Status12Enum

status_12 = Status12Enum.INACTIVE
```

