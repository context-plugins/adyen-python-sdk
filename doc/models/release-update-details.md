
# Release Update Details

*This model accepts additional fields of type Any.*

## Structure

`ReleaseUpdateDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type62`](../../doc/models/type-62.md) | Optional | - |
| `update_at_first_maintenance_call` | `bool` | Optional | Boolean flag that tells if the terminal should update at the first next maintenance call. If false, terminal will update on its configured reboot time. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.release_update_details import ReleaseUpdateDetails
from adyen.models.type_62 import Type62

release_update_details = ReleaseUpdateDetails(
    mtype=Type62.RELEASEUPDATE,
    update_at_first_maintenance_call=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

