
# Timeouts

*This model accepts additional fields of type Any.*

## Structure

`Timeouts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_active_to_sleep` | `int` | Optional | Indicates the number of seconds of inactivity after which the terminal display goes into sleep mode. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.timeouts import Timeouts

timeouts = Timeouts(
    from_active_to_sleep=94,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

