
# Duration 1

The duration, which you can specify in hours, days, weeks, or months. The maximum duration is 90 days or an equivalent in other units. Required when the `type` is **rolling** or **sliding**.

*This model accepts additional fields of type Any.*

## Structure

`Duration1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unit` | [`Unit`](../../doc/models/unit.md) | Optional | - |
| `value` | `int` | Optional | The length of time by the unit. For example, 5 days.<br><br>The maximum duration is 90 days or an equivalent in other units. For example, 3 months. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.duration_1 import Duration1
from adyen.models.unit import Unit

duration_1 = Duration1(
    unit=Unit.HOURS,
    value=214,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

