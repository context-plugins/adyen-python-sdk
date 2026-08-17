
# Limit Status Enum

The status of the transfer limit. Possible values:

* **active**: the limit is currently active.
* **inactive**: the limit is currently inactive.
* **pendingSCA**: the limit is pending until your user performs SCA.
* **scheduled**: the limit is scheduled to become active at a future date.

## Enumeration

`LimitStatusEnum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `INACTIVE` |
| `PENDINGSCA` |
| `SCHEDULED` |

## Example

```python
from adyen.models.limit_status_enum import LimitStatusEnum

limit_status = LimitStatusEnum.PENDINGSCA
```

