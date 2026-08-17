
# Day of Week Restriction

## Structure

`DayOfWeekRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value1Enum]`](../../doc/models/value-1-enum.md) | Optional | List of days of the week.<br><br>Possible values: **monday**, **tuesday**, **wednesday**, **thursday**, **friday**, **saturday**, **sunday**. |

## Example

```python
from adyen.models.day_of_week_restriction import DayOfWeekRestriction
from adyen.models.value_1_enum import Value1Enum

day_of_week_restriction = DayOfWeekRestriction(
    operation='operation2',
    value=[
        Value1Enum.WEDNESDAY,
        Value1Enum.FRIDAY,
        Value1Enum.MONDAY
    ]
)
```

