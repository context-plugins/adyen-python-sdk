
# Identity 2

Contains the identity details of the party.

*This model accepts additional fields of type Any.*

## Structure

`Identity2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_legal_name` | `str` | Required | The complete legal name of the individual or entity. |
| `name` | `str` | Required | A commonly used or human-readable name for the individual or entity. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.identity_2 import Identity2

identity_2 = Identity2(
    full_legal_name='fullLegalName8',
    name='name0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

