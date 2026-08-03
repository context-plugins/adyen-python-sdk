
# Source Account Types Restriction 1

Contains a list of source account types and how they must be evaluated.

Supported operations: **anyMatch**, **noneMatch**.

Supported value inputs:

- **balanceAccount**
- **businessAccount**.

*This model accepts additional fields of type Any.*

## Structure

`SourceAccountTypesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value5]`](../../doc/models/value-5.md) | Optional | The list of source account types to be evaluated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.source_account_types_restriction_1 import SourceAccountTypesRestriction1
from adyen.models.value_5 import Value5

source_account_types_restriction_1 = SourceAccountTypesRestriction1(
    operation='operation2',
    value=[
        Value5.BALANCEACCOUNT,
        Value5.BUSINESSACCOUNT,
        Value5.BALANCEACCOUNT
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

