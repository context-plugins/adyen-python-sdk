
# Ticket Response Info

## Structure

`TicketResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `requestor_id` | `str` | Optional | Ticket requestorId |

## Example

```python
from adyen.models.ticket_response_info import TicketResponseInfo

ticket_response_info = TicketResponseInfo(
    requestor_id='requestorId0'
)
```

