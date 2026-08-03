
# Host Status

Indicate the reachability of the host by the POI Terminal.
State of a Host.

*This model accepts additional fields of type Any.*

## Structure

`HostStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquirer_id` | `int` | Required | Identification of the Acquirer. |
| `is_reachable_flag` | `bool` | Optional | Indicate if a Host is reachable.<br><br>**Default**: `True` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.host_status import HostStatus

host_status = HostStatus(
    acquirer_id=220,
    is_reachable_flag=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

