
# Processing Types Restriction

*This model accepts additional fields of type Any.*

## Structure

`ProcessingTypesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value4]`](../../doc/models/value-4.md) | Optional | List of processing types.<br><br>Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **recurring**, **token**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.processing_types_restriction import ProcessingTypesRestriction
from adyen.models.value_4 import Value4

processing_types_restriction = ProcessingTypesRestriction(
    operation='operation4',
    value=[
        Value4.POS
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

