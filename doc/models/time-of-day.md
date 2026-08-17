
# Time of Day

## Structure

`TimeOfDay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end_time` | `str` | Optional | The end time in a time-only ISO-8601 extended offset format. For example: **08:00:00+02:00**, **22:30:00-03:00**. |
| `start_time` | `str` | Optional | The start time in a time-only ISO-8601 extended offset format. For example: **08:00:00+02:00**, **22:30:00-03:00**. |

## Example

```python
from adyen.models.time_of_day import TimeOfDay

time_of_day = TimeOfDay(
    end_time='endTime0',
    start_time='startTime2'
)
```

