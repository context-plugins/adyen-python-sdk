
# Time of Day Restriction 1

A start and end time in a time-only ISO-8601 extended offset format. Supported operations: **equals**, **notEquals**.

*This model accepts additional fields of type Any.*

## Structure

`TimeOfDayRestriction1`

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
from adyen.models.time_of_day_restriction_1 import TimeOfDayRestriction1

time_of_day_restriction_1 = TimeOfDayRestriction1(
    operation='operation8',
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

