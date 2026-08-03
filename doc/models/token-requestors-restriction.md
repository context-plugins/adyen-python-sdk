
# Token Requestors Restriction

*This model accepts additional fields of type Any.*

## Structure

`TokenRequestorsRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `List[str]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.token_requestors_restriction import TokenRequestorsRestriction

token_requestors_restriction = TokenRequestorsRestriction(
    operation='operation2',
    value=[
        'value6'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

