
# Status 17

The status of the store. Possible values are:

- **active**. This value is assigned automatically when a store is created.
- **inactive**. The terminals under the store are blocked from accepting new transactions, but capturing outstanding transactions is still possible.
- **closed**. This status is irreversible. The terminals under the store are reassigned to the merchant inventory.

## Enumeration

`Status17`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |

## Example

```python
from adyen.models.status_17 import Status17

status_17 = Status17.CLOSED
```

