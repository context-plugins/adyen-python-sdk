
# Target Update 2

The type and ID of the resource about whose balance changes you want to be notified.

*This model accepts additional fields of type Any.*

## Structure

`TargetUpdate2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the `target.type`. This can be the ID of your:<br><br>* balance platform<br>* account holder<br>* account holder's balance account<br><br>**Constraints**: *Minimum Length*: `1` |
| `mtype` | [`Type18`](../../doc/models/type-18.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.target_update_2 import TargetUpdate2
from adyen.models.type_18 import Type18

target_update_2 = TargetUpdate2(
    id='id8',
    mtype=Type18.BALANCEPLATFORM,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

