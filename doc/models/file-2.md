
# File 2

For `eap` **tls**. The certificate chain for the terminals. All terminals in the same network will use the same EAP client certificate.

*This model accepts additional fields of type Any.*

## Structure

`File2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `str` | Required | The certificate content converted to a Base64-encoded string. |
| `name` | `str` | Required | The name of the certificate. Must be unique across Wi-Fi profiles. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.file_2 import File2

file_2 = File2(
    data='data6',
    name='name6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

