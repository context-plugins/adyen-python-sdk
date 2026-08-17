
# Source Account Types Restriction

## Structure

`SourceAccountTypesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value5Enum]`](../../doc/models/value-5-enum.md) | Optional | The list of source account types to be evaluated. |

## Example

```python
from adyen.models.source_account_types_restriction import SourceAccountTypesRestriction
from adyen.models.value_5_enum import Value5Enum

source_account_types_restriction = SourceAccountTypesRestriction(
    operation='operation2',
    value=[
        Value5Enum.BALANCEACCOUNT
    ]
)
```

