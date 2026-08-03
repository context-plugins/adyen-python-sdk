
# Force Reboot Details

*This model accepts additional fields of type Any.*

## Structure

`ForceRebootDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type210`](../../doc/models/type-210.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.force_reboot_details import ForceRebootDetails
from adyen.models.type_210 import Type210

force_reboot_details = ForceRebootDetails(
    mtype=Type210.FORCEREBOOT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

