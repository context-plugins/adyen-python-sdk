
# Ticket Info 2

Details to provide if `type` is **ticket** (Edenred Brazil).

## Structure

`TicketInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `requestor_id` | `str` | Optional | Ticket requestorId |

## Example

```python
from adyen.models.ticket_info_2 import TicketInfo2

ticket_info_2 = TicketInfo2(
    requestor_id='requestorId8'
)
```

