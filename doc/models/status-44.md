
# Status 44

The status of the transfer.

Possible values:

- **pending**: the transfer is under internal review by Adyen.

- **failed**: the transfer failed Adyen's internal review. For details, see `reason`.

## Enumeration

`Status44`

## Fields

| Name |
|  --- |
| `PENDING` |
| `FAILED` |

## Example

```python
from adyen.models.status_44 import Status44

status_44 = Status44.PENDING
```

