
# Time of Day

*This model accepts additional fields of type Any.*

## Structure

`TimeOfDay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end_time` | `str` | Optional | The end time in a time-only ISO-8601 extended offset format. For example: **08:00:00+02:00**, **22:30:00-03:00**. |
| `start_time` | `str` | Optional | The start time in a time-only ISO-8601 extended offset format. For example: **08:00:00+02:00**, **22:30:00-03:00**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.time_of_day import TimeOfDay

time_of_day = TimeOfDay(
    end_time='endTime0',
    start_time='startTime2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

