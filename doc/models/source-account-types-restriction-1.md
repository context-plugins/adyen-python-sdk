
# Source Account Types Restriction 1

Contains a list of source account types and how they must be evaluated.

Supported operations: **anyMatch**, **noneMatch**.

Supported value inputs:

- **balanceAccount**
- **businessAccount**.

## Structure

`SourceAccountTypesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value5Enum]`](../../doc/models/value-5-enum.md) | Optional | The list of source account types to be evaluated. |

## Example

```python
from adyen.models.source_account_types_restriction_1 import SourceAccountTypesRestriction1
from adyen.models.value_5_enum import Value5Enum

source_account_types_restriction_1 = SourceAccountTypesRestriction1(
    operation='operation2',
    value=[
        Value5Enum.BALANCEACCOUNT,
        Value5Enum.BUSINESSACCOUNT,
        Value5Enum.BALANCEACCOUNT
    ]
)
```

