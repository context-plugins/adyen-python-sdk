
# Target Update

*This model accepts additional fields of type Any.*

## Structure

`TargetUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the `target.type`. This can be the ID of your:<br><br>* balance platform<br>* account holder<br>* account holder's balance account<br><br>**Constraints**: *Minimum Length*: `1` |
| `mtype` | [`Type18`](../../doc/models/type-18.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.target_update import TargetUpdate
from adyen.models.type_18 import Type18

target_update = TargetUpdate(
    id='id4',
    mtype=Type18.ACCOUNTHOLDER,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

