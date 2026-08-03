
# Day of Week Restriction 1

List of week days and the operation. Supported operations: **anyMatch**, **noneMatch**.

*This model accepts additional fields of type Any.*

## Structure

`DayOfWeekRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value1]`](../../doc/models/value-1.md) | Optional | List of days of the week.<br><br>Possible values: **monday**, **tuesday**, **wednesday**, **thursday**, **friday**, **saturday**, **sunday**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.day_of_week_restriction_1 import DayOfWeekRestriction1
from adyen.models.value_1 import Value1

day_of_week_restriction_1 = DayOfWeekRestriction1(
    operation='operation8',
    value=[
        Value1.THURSDAY,
        Value1.TUESDAY,
        Value1.WEDNESDAY
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

