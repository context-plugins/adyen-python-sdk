
# Identity

*This model accepts additional fields of type Any.*

## Structure

`Identity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_legal_name` | `str` | Required | The complete legal name of the individual or entity. |
| `name` | `str` | Required | A commonly used or human-readable name for the individual or entity. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.identity import Identity

identity = Identity(
    full_legal_name='fullLegalName2',
    name='name4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

