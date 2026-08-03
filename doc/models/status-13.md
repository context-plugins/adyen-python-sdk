
# Status 13

The status of the request for PIN change.

Possible values: **completed**, **pending**, **unavailable**.

## Enumeration

`Status13`

## Fields

| Name |
|  --- |
| `COMPLETED` |
| `PENDING` |
| `UNAVAILABLE` |

## Example

```python
from adyen.models.status_13 import Status13

status_13 = Status13.UNAVAILABLE
```

