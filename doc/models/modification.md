
# Modification

*This model accepts additional fields of type Any.*

## Structure

`Modification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `direction` | `str` | Optional | The direction of the money movement. |
| `id` | `str` | Optional | Our reference for the modification. |
| `reference` | `str` | Optional | Your reference for the modification, used internally within your platform. |
| `status` | [`Status25`](../../doc/models/status-25.md) | Optional | - |
| `mtype` | `str` | Optional | The type of transfer modification. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.modification import Modification
from adyen.models.status_25 import Status25

modification = Modification(
    direction='direction8',
    id='id2',
    reference='reference2',
    status=Status25.DEPOSITCORRECTION,
    mtype='type8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

