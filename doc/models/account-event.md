
# Account Event

*This model accepts additional fields of type Any.*

## Structure

`AccountEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event` | [`Event`](../../doc/models/event.md) | Optional | - |
| `execution_date` | `datetime` | Optional | The date on which the event will take place. |
| `reason` | `str` | Optional | The reason why this event has been created. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.account_event import AccountEvent
from adyen.models.event import Event

account_event = AccountEvent(
    event=Event.INACTIVATEACCOUNT,
    execution_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    reason='reason0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

