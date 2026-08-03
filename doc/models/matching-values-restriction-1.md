
# Matching Values Restriction 1

Checks if a user has recently made multiple transfers with the specified values.

To use this restriction, you must:

- Set the rule `type` to **velocity**.

- Specify a time `interval`.

- Specify a number of `matchingTransactions`.

Supported operation: **allMatch**.

Supported value inputs:

- **merchantId** and **acquirerId**
- **amount** and **currency**
- **merchantName**.

*This model accepts additional fields of type Any.*

## Structure

`MatchingValuesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value3]`](../../doc/models/value-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.matching_values_restriction_1 import MatchingValuesRestriction1
from adyen.models.value_3 import Value3

matching_values_restriction_1 = MatchingValuesRestriction1(
    operation='operation2',
    value=[
        Value3.AMOUNT,
        Value3.CURRENCY
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

