
# Status 71

The status of the transaction.

Possible values:

* **pending**: The transaction is still pending.

* **booked**: The transaction has been booked to the balance account.

## Enumeration

`Status71`

## Fields

| Name |
|  --- |
| `BOOKED` |
| `PENDING` |

## Example

```python
from adyen.models.status_71 import Status71

status_71 = Status71.BOOKED
```

