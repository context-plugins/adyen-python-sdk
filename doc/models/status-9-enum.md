
# Status 9 Enum

The status of the account holder.

Possible values:

* **active**: The account holder is active and allowed to use its capabilities. This is the initial status for account holders and balance accounts. You can change this status to **suspended** or **closed**.

* **suspended**: The account holder is temporarily disabled and payouts are blocked. You can change this status to **active** or **closed**.

* **closed**: The account holder and all of its capabilities are permanently disabled. This is a final status and cannot be changed.

## Enumeration

`Status9Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `SUSPENDED` |

## Example

```python
from adyen.models.status_9_enum import Status9Enum

status_9 = Status9Enum.CLOSED
```

