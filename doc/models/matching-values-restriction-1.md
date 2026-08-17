
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

## Structure

`MatchingValuesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value3Enum]`](../../doc/models/value-3-enum.md) | Optional | - |

## Example

```python
from adyen.models.matching_values_restriction_1 import MatchingValuesRestriction1
from adyen.models.value_3_enum import Value3Enum

matching_values_restriction_1 = MatchingValuesRestriction1(
    operation='operation2',
    value=[
        Value3Enum.AMOUNT,
        Value3Enum.CURRENCY
    ]
)
```

