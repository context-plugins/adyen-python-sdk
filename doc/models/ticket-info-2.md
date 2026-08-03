
# Ticket Info 2

Details to provide if `type` is **ticket** (Edenred Brazil).

*This model accepts additional fields of type Any.*

## Structure

`TicketInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `requestor_id` | `str` | Optional | Ticket requestorId |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.ticket_info_2 import TicketInfo2

ticket_info_2 = TicketInfo2(
    requestor_id='requestorId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

