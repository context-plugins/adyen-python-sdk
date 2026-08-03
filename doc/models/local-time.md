
# Local Time

*This model accepts additional fields of type Any.*

## Structure

`LocalTime`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hour` | `int` | Optional | - |
| `minute` | `int` | Optional | - |
| `nano` | `int` | Optional | - |
| `second` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.local_time import LocalTime

local_time = LocalTime(
    hour=180,
    minute=182,
    nano=206,
    second=244,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

