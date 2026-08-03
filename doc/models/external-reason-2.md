
# External Reason 2

The external reason of this transfer.

*This model accepts additional fields of type Any.*

## Structure

`ExternalReason2`

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

from adyen.models.external_reason_2 import ExternalReason2

external_reason_2 = ExternalReason2(
    code='code4',
    description='description6',
    namespace='namespace6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

