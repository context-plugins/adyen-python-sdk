
# Status 5

The status of the account holder.

Possible values:

* **active**: The account holder is active and allowed to use its capabilities. This is the initial status for account holders and balance accounts. You can change this status to **suspended** or **closed**.

* **suspended**: The account holder is temporarily disabled and payouts are blocked. You can change this status to **active** or **closed**.

* **closed**: The account holder and all of its capabilities are permanently disabled. This is a final status and cannot be changed.

## Enumeration

`Status5`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `SUSPENDED` |

## Example

```python
from adyen.models.status_5 import Status5

status_5 = Status5.SUSPENDED
```

