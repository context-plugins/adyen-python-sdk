
# Merchant Names Restriction

## Structure

`MerchantNamesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[StringMatch]`](../../doc/models/string-match.md) | Optional | - |

## Example

```python
from adyen.models.merchant_names_restriction import MerchantNamesRestriction
from adyen.models.operation_enum import OperationEnum
from adyen.models.string_match import StringMatch

merchant_names_restriction = MerchantNamesRestriction(
    operation='operation6',
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

