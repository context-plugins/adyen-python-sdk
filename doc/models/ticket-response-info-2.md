
# Ticket Response Info 2

**ticket** (Edenred Brazil) details

*This model accepts additional fields of type Any.*

## Structure

`TicketResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `requestor_id` | `str` | Optional | Ticket requestorId |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.ticket_response_info_2 import TicketResponseInfo2

ticket_response_info_2 = TicketResponseInfo2(
    requestor_id='requestorId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

