
# Status 13 Enum

The status of the request for PIN change.

Possible values: **completed**, **pending**, **unavailable**.

## Enumeration

`Status13Enum`

## Fields

| Name |
|  --- |
| `COMPLETED` |
| `PENDING` |
| `UNAVAILABLE` |

## Example

```python
from adyen.models.status_13_enum import Status13Enum

status_13 = Status13Enum.UNAVAILABLE
```

