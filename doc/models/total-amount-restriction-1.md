
# Total Amount Restriction 1

The total amount and the operation.

Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.

*This model accepts additional fields of type Any.*

## Structure

`TotalAmountRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`Value7`](../../doc/models/value-7.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.total_amount_restriction_1 import TotalAmountRestriction1
from adyen.models.value_7 import Value7

total_amount_restriction_1 = TotalAmountRestriction1(
    operation='operation6',
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

