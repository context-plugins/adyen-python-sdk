
# Data Center

*This model accepts additional fields of type Any.*

## Structure

`DataCenter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `live_prefix` | `str` | Optional | The unique [live URL prefix](https://docs.adyen.com/development-resources/live-endpoints#live-url-prefix) for your live endpoint. Each data center has its own live URL prefix.<br><br>This field is empty for requests made in the test environment. |
| `name` | `str` | Optional | The name assigned to a data center, for example **EU** for the European data center. Possible values are:<br><br>* **default**: the European data center. This value is always returned in the test environment.<br>* **AU**<br>* **EU**<br>* **US** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.data_center import DataCenter

data_center = DataCenter(
    live_prefix='livePrefix8',
    name='name2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

