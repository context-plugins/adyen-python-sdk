
# Duration

*This model accepts additional fields of type Any.*

## Structure

`Duration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unit` | [`Unit`](../../doc/models/unit.md) | Optional | - |
| `value` | `int` | Optional | The length of time by the unit. For example, 5 days.<br><br>The maximum duration is 90 days or an equivalent in other units. For example, 3 months. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.duration import Duration
from adyen.models.unit import Unit

duration = Duration(
    unit=Unit.WEEKS,
    value=176,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

