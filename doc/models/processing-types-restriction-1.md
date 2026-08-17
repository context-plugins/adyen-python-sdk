
# Processing Types Restriction 1

List of processing types and the operation.

Supported operations: **anyMatch**, **noneMatch**.

## Structure

`ProcessingTypesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value4Enum]`](../../doc/models/value-4-enum.md) | Optional | List of processing types.<br><br>Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **recurring**, **token**. |

## Example

```python
from adyen.models.processing_types_restriction_1 import ProcessingTypesRestriction1
from adyen.models.value_4_enum import Value4Enum

processing_types_restriction_1 = ProcessingTypesRestriction1(
    operation='operation2',
    value=[
        Value4Enum.TOKEN,
        Value4Enum.UNKNOWN
    ]
)
```

