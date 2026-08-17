
# Status 15 Enum

The status of the transfer.

Possible values:

- **credited**: the funds are credited to your user's transfer instrument or bank account.- **accepted**: the request is accepted by the integration.

## Enumeration

`Status15Enum`

## Fields

| Name |
|  --- |
| `CREDITED` |
| `ACCEPTED` |

## Example

```python
from adyen.models.status_15_enum import Status15Enum

status_15 = Status15Enum.CREDITED
```

