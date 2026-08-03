
# Total Amount Restriction

*This model accepts additional fields of type Any.*

## Structure

`TotalAmountRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`Value7`](../../doc/models/value-7.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.total_amount_restriction import TotalAmountRestriction
from adyen.models.value_7 import Value7

total_amount_restriction = TotalAmountRestriction(
    operation='operation0',
    value=Value7(
        currency='currency2',
        value=128,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

