
# Ticket Response Info

*This model accepts additional fields of type Any.*

## Structure

`TicketResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `requestor_id` | `str` | Optional | Ticket requestorId |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.ticket_response_info import TicketResponseInfo

ticket_response_info = TicketResponseInfo(
    requestor_id='requestorId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

