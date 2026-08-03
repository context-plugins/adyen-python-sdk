
# Notification Event Configuration

*This model accepts additional fields of type Any.*

## Structure

`NotificationEventConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventType`](../../doc/models/event-type.md) | Required | - |
| `include_mode` | [`IncludeMode`](../../doc/models/include-mode.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.event_type import EventType
from adyen.models.include_mode import IncludeMode
from adyen.models.notification_event_configuration import NotificationEventConfiguration

notification_event_configuration = NotificationEventConfiguration(
    event_type=EventType.BENEFICIARY_SETUP,
    include_mode=IncludeMode.EXCLUDE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

