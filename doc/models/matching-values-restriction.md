
# Matching Values Restriction

## Structure

`MatchingValuesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value3Enum]`](../../doc/models/value-3-enum.md) | Optional | - |

## Example

```python
from adyen.models.matching_values_restriction import MatchingValuesRestriction
from adyen.models.value_3_enum import Value3Enum

matching_values_restriction = MatchingValuesRestriction(
    operation='operation6',
    value=[
        Value3Enum.ACQUIRERID,
        Value3Enum.AMOUNT,
        Value3Enum.CURRENCY
    ]
)
```

