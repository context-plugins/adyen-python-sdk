
# Schedule 21

Contains the details about the schedule that determines when the top up is executed.

*This model accepts additional fields of type Any.*

## Structure

`Schedule21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`ScheduleType1`](../../doc/models/schedule-type-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.schedule_21 import Schedule21
from adyen.models.schedule_type_1 import ScheduleType1

schedule_21 = Schedule21(
    mtype=ScheduleType1.WEEKDAYS,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

