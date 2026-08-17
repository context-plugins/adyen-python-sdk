
# Status 44 Enum

The status of the transfer.

Possible values:

- **pending**: the transfer is under internal review by Adyen.

- **failed**: the transfer failed Adyen's internal review. For details, see `reason`.

## Enumeration

`Status44Enum`

## Fields

| Name |
|  --- |
| `PENDING` |
| `FAILED` |

## Example

```python
from adyen.models.status_44_enum import Status44Enum

status_44 = Status44Enum.PENDING
```

