
# Patchable Schedule

*This model accepts additional fields of type Any.*

## Structure

`PatchableSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`ScheduleType1`](../../doc/models/schedule-type-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.patchable_schedule import PatchableSchedule
from adyen.models.schedule_type_1 import ScheduleType1

patchable_schedule = PatchableSchedule(
    mtype=ScheduleType1.MONTHLY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

