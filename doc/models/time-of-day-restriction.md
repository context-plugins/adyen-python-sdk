
# Time of Day Restriction

*This model accepts additional fields of type Any.*

## Structure

`TimeOfDayRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`TimeOfDay`](../../doc/models/time-of-day.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.time_of_day import TimeOfDay
from adyen.models.time_of_day_restriction import TimeOfDayRestriction

time_of_day_restriction = TimeOfDayRestriction(
    operation='operation6',
    value=TimeOfDay(
        end_time='endTime6',
        start_time='startTime8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

