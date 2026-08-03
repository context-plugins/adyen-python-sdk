
# External Reason

*This model accepts additional fields of type Any.*

## Structure

`ExternalReason`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The reason code. |
| `description` | `str` | Optional | The description of the reason code. |
| `namespace` | `str` | Optional | The namespace for the reason code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.external_reason import ExternalReason

external_reason = ExternalReason(
    code='code6',
    description='description8',
    namespace='namespace4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

