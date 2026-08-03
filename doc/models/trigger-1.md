
# Trigger 1

The condition that triggers the top-up. This can be a recurring schedule or a minimum balance threshold.

*This model accepts additional fields of type Any.*

## Structure

`Trigger1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schedule` | [`Schedule2`](../../doc/models/schedule-2.md) | Optional | - |
| `threshold` | [`Threshold2`](../../doc/models/threshold-2.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.schedule_2 import Schedule2
from adyen.models.schedule_type_1 import ScheduleType1
from adyen.models.threshold_2 import Threshold2
from adyen.models.trigger_1 import Trigger1

trigger_1 = Trigger1(
    threshold=Threshold2(
        currency='currency8',
        value=32,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    schedule=Schedule2(
        mtype=ScheduleType1.WEEKDAYS,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

