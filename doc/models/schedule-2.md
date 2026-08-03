
# Schedule 2

*This model accepts additional fields of type Any.*

## Structure

`Schedule2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`ScheduleType1`](../../doc/models/schedule-type-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.schedule_2 import Schedule2
from adyen.models.schedule_type_1 import ScheduleType1

schedule_2 = Schedule2(
    mtype=ScheduleType1.WEEKDAYS,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

