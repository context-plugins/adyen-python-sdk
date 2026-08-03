
# Target 3

The resource about whose balance change you want to get notified.

*This model accepts additional fields of type Any.*

## Structure

`Target3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The unique identifier of the `target.type`. This can be the ID of your:<br><br>* balance platform<br>* account holder<br>* account holder's balance account<br><br>**Constraints**: *Minimum Length*: `1` |
| `mtype` | [`Type18`](../../doc/models/type-18.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.target_3 import Target3
from adyen.models.type_18 import Type18

target_3 = Target3(
    id='id6',
    mtype=Type18.BALANCEACCOUNT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

