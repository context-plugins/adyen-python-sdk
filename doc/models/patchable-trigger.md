
# Patchable Trigger

*This model accepts additional fields of type Any.*

## Structure

`PatchableTrigger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schedule` | [PatchableSchedule](../../doc/models/patchable-schedule.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `threshold` | [`Threshold3`](../../doc/models/threshold-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.patchable_schedule import PatchableSchedule
from adyen.models.patchable_trigger import PatchableTrigger
from adyen.models.schedule_type_1 import ScheduleType1
from adyen.models.threshold_3 import Threshold3

patchable_trigger = PatchableTrigger(
    schedule=PatchableSchedule(
        mtype=ScheduleType1.MONTHLY,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    threshold=Threshold3(
        currency='currency8',
        value=32,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

