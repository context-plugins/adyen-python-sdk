
# Processing Types Restriction

## Structure

`ProcessingTypesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value4Enum]`](../../doc/models/value-4-enum.md) | Optional | List of processing types.<br><br>Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **recurring**, **token**. |

## Example

```python
from adyen.models.processing_types_restriction import ProcessingTypesRestriction
from adyen.models.value_4_enum import Value4Enum

processing_types_restriction = ProcessingTypesRestriction(
    operation='operation4',
    value=[
        Value4Enum.POS
    ]
)
```

