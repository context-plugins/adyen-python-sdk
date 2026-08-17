
# Day of Week Restriction 1

List of week days and the operation. Supported operations: **anyMatch**, **noneMatch**.

## Structure

`DayOfWeekRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value1Enum]`](../../doc/models/value-1-enum.md) | Optional | List of days of the week.<br><br>Possible values: **monday**, **tuesday**, **wednesday**, **thursday**, **friday**, **saturday**, **sunday**. |

## Example

```python
from adyen.models.day_of_week_restriction_1 import DayOfWeekRestriction1
from adyen.models.value_1_enum import Value1Enum

day_of_week_restriction_1 = DayOfWeekRestriction1(
    operation='operation8',
    value=[
        Value1Enum.THURSDAY,
        Value1Enum.TUESDAY,
        Value1Enum.WEDNESDAY
    ]
)
```

