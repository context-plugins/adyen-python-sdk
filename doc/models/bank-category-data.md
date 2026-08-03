
# Bank Category Data

*This model accepts additional fields of type Any.*

## Structure

`BankCategoryData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `priority` | [`Priority`](../../doc/models/priority.md) | Optional | - |
| `mtype` | [`Type312`](../../doc/models/type-312.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_category_data import BankCategoryData
from adyen.models.priority import Priority
from adyen.models.type_312 import Type312

bank_category_data = BankCategoryData(
    priority=Priority.INSTANT,
    mtype=Type312.BANK,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

