
# Time of Day Restriction

## Structure

`TimeOfDayRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`TimeOfDay`](../../doc/models/time-of-day.md) | Optional | - |

## Example

```python
from adyen.models.time_of_day import TimeOfDay
from adyen.models.time_of_day_restriction import TimeOfDayRestriction

time_of_day_restriction = TimeOfDayRestriction(
    operation='operation6',
    value=TimeOfDay(
        end_time='endTime6',
        start_time='startTime8'
    )
)
```

