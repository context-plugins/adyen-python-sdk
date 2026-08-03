
# Status 16

The new status of the network token. Possible values: **active**, **suspended**, **closed**. The **closed** status is final and cannot be changed.

## Enumeration

`Status16`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `SUSPENDED` |
| `CLOSED` |

## Example

```python
from adyen.models.status_16 import Status16

status_16 = Status16.SUSPENDED
```

