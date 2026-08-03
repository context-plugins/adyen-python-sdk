
# Limit Status

The status of the transfer limit. Possible values:

* **active**: the limit is currently active.
* **inactive**: the limit is currently inactive.
* **pendingSCA**: the limit is pending until your user performs SCA.
* **scheduled**: the limit is scheduled to become active at a future date.

## Enumeration

`LimitStatus`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `INACTIVE` |
| `PENDINGSCA` |
| `SCHEDULED` |

## Example

```python
from adyen.models.limit_status import LimitStatus

limit_status = LimitStatus.PENDINGSCA
```

