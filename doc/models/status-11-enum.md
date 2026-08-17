
# Status 11 Enum

The status of the store. Possible values are:

- **active**. This value is assigned automatically when a store is created.
- **inactive**. The terminals under the store are blocked from accepting new transactions, but capturing outstanding transactions is still possible.
- **closed**. This status is irreversible. The terminals under the store are reassigned to the merchant inventory.

## Enumeration

`Status11Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |

## Example

```python
from adyen.models.status_11_enum import Status11Enum

status_11 = Status11Enum.INACTIVE
```

