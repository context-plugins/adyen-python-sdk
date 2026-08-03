
# Same Amount Restriction

*This model accepts additional fields of type Any.*

## Structure

`SameAmountRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `bool` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.same_amount_restriction import SameAmountRestriction

same_amount_restriction = SameAmountRestriction(
    operation='operation0',
    value=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

