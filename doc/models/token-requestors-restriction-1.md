
# Token Requestors Restriction 1

List of token requestor IDs and the operation.

Supported operations: **anyMatch**, **noneMatch**.

*This model accepts additional fields of type Any.*

## Structure

`TokenRequestorsRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `List[str]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.token_requestors_restriction_1 import TokenRequestorsRestriction1

token_requestors_restriction_1 = TokenRequestorsRestriction1(
    operation='operation0',
    value=[
        'value4',
        'value5',
        'value6'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

