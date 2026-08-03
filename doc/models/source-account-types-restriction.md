
# Source Account Types Restriction

*This model accepts additional fields of type Any.*

## Structure

`SourceAccountTypesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value5]`](../../doc/models/value-5.md) | Optional | The list of source account types to be evaluated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.source_account_types_restriction import SourceAccountTypesRestriction
from adyen.models.value_5 import Value5

source_account_types_restriction = SourceAccountTypesRestriction(
    operation='operation2',
    value=[
        Value5.BALANCEACCOUNT
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

