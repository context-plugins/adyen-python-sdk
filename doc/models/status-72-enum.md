
# Status 72 Enum

The status of the transaction.

Possible values:

* **pending**: The transaction is still pending.

* **booked**: The transaction has been booked to the balance account.

## Enumeration

`Status72Enum`

## Fields

| Name |
|  --- |
| `BOOKED` |
| `PENDING` |

## Example

```python
from adyen.models.status_72_enum import Status72Enum

status_72 = Status72Enum.BOOKED
```

