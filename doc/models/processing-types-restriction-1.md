
# Processing Types Restriction 1

List of processing types and the operation.

Supported operations: **anyMatch**, **noneMatch**.

*This model accepts additional fields of type Any.*

## Structure

`ProcessingTypesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value4]`](../../doc/models/value-4.md) | Optional | List of processing types.<br><br>Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **recurring**, **token**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.processing_types_restriction_1 import ProcessingTypesRestriction1
from adyen.models.value_4 import Value4

processing_types_restriction_1 = ProcessingTypesRestriction1(
    operation='operation2',
    value=[
        Value4.TOKEN,
        Value4.UNKNOWN
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

