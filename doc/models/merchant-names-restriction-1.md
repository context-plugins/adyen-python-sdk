
# Merchant Names Restriction 1

List of names that will be compared to the merchant name according to the matching type.

Supported operations: **anyMatch**, **noneMatch**.

## Structure

`MerchantNamesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[StringMatch]`](../../doc/models/string-match.md) | Optional | - |

## Example

```python
from adyen.models.merchant_names_restriction_1 import MerchantNamesRestriction1
from adyen.models.operation_enum import OperationEnum
from adyen.models.string_match import StringMatch

merchant_names_restriction_1 = MerchantNamesRestriction1(
    operation='operation4',
    value=[
        StringMatch(
            operation=OperationEnum.ISEQUALTO,
            value='value4'
        ),
        StringMatch(
            operation=OperationEnum.ISEQUALTO,
            value='value4'
        ),
        StringMatch(
            operation=OperationEnum.ISEQUALTO,
            value='value4'
        )
    ]
)
```

