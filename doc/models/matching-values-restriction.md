
# Matching Values Restriction

*This model accepts additional fields of type Any.*

## Structure

`MatchingValuesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value3]`](../../doc/models/value-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.matching_values_restriction import MatchingValuesRestriction
from adyen.models.value_3 import Value3

matching_values_restriction = MatchingValuesRestriction(
    operation='operation6',
    value=[
        Value3.ACQUIRERID,
        Value3.AMOUNT,
        Value3.CURRENCY
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

