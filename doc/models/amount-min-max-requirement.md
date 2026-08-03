
# Amount Min Max Requirement

*This model accepts additional fields of type Any.*

## Structure

`AmountMinMaxRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies the eligible amounts for a particular route. |
| `max` | `int` | Optional | Maximum amount. |
| `min` | `int` | Optional | Minimum amount. |
| `mtype` | [`Type810`](../../doc/models/type-810.md) | Required | **amountMinMaxRequirement** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_min_max_requirement import AmountMinMaxRequirement
from adyen.models.type_810 import Type810

amount_min_max_requirement = AmountMinMaxRequirement(
    mtype=Type810.AMOUNTMINMAXREQUIREMENT,
    description='description6',
    max=222,
    min=48,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

