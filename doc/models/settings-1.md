
# Settings 1

General Wi-Fi settings.

*This model accepts additional fields of type Any.*

## Structure

`Settings1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band` | `str` | Optional | The preferred Wi-Fi band, for use if the terminals support multiple bands. Possible values: All, 2.4GHz, 5GHz. |
| `roaming` | `bool` | Optional | Indicates whether roaming is enabled on the terminals. |
| `timeout` | `int` | Optional | The connection time-out in seconds. Minimum value: 0. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.settings_1 import Settings1

settings_1 = Settings1(
    band='band4',
    roaming=False,
    timeout=152,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

