
# Day of Week Restriction

*This model accepts additional fields of type Any.*

## Structure

`DayOfWeekRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value1]`](../../doc/models/value-1.md) | Optional | List of days of the week.<br><br>Possible values: **monday**, **tuesday**, **wednesday**, **thursday**, **friday**, **saturday**, **sunday**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.day_of_week_restriction import DayOfWeekRestriction
from adyen.models.value_1 import Value1

day_of_week_restriction = DayOfWeekRestriction(
    operation='operation2',
    value=[
        Value1.WEDNESDAY,
        Value1.FRIDAY,
        Value1.MONDAY
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

