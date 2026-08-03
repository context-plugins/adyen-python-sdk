
# Local Time 2

The time when the payout funds are settled in your user's transfer instrument.

*This model accepts additional fields of type Any.*

## Structure

`LocalTime2`

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

from adyen.models.local_time_2 import LocalTime2

local_time_2 = LocalTime2(
    hour=48,
    minute=50,
    nano=74,
    second=144,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

