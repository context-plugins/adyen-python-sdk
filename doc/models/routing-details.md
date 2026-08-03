
# Routing Details

*This model accepts additional fields of type Any.*

## Structure

`RoutingDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `detail` | `str` | Optional | A human-readable explanation specific to this occurrence of the problem. |
| `error_code` | `str` | Optional | A code that identifies the problem type. |
| `priority` | [`Priority`](../../doc/models/priority.md) | Optional | - |
| `title` | `str` | Optional | A short, human-readable summary of the problem type. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.priority import Priority
from adyen.models.routing_details import RoutingDetails

routing_details = RoutingDetails(
    detail='detail8',
    error_code='errorCode8',
    priority=Priority.REGULAR,
    title='title2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

