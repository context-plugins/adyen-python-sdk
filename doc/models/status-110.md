
# Status 110

The status of the transfer.

Possible values:

- **credited**: the funds are credited to your user's transfer instrument or bank account.- **accepted**: the request is accepted by the integration.

## Enumeration

`Status110`

## Fields

| Name |
|  --- |
| `CREDITED` |
| `ACCEPTED` |

## Example

```python
from adyen.models.status_110 import Status110

status_110 = Status110.CREDITED
```

