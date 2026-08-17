
# Status 16 Enum

The new status of the network token. Possible values: **active**, **suspended**, **closed**. The **closed** status is final and cannot be changed.

## Enumeration

`Status16Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `SUSPENDED` |
| `CLOSED` |

## Example

```python
from adyen.models.status_16_enum import Status16Enum

status_16 = Status16Enum.SUSPENDED
```

