
# Merchant Names Restriction

*This model accepts additional fields of type Any.*

## Structure

`MerchantNamesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[StringMatch]`](../../doc/models/string-match.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.merchant_names_restriction import MerchantNamesRestriction
from adyen.models.operation import Operation
from adyen.models.string_match import StringMatch

merchant_names_restriction = MerchantNamesRestriction(
    operation='operation6',
    value=[
        StringMatch(
            operation=Operation.ISEQUALTO,
            value='value4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        StringMatch(
            operation=Operation.ISEQUALTO,
            value='value4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        StringMatch(
            operation=Operation.ISEQUALTO,
            value='value4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

