
# File 4

For `eap` **tls**. The EAP intermediate certificate.

## Structure

`File4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `str` | Required | The certificate content converted to a Base64-encoded string. |
| `name` | `str` | Required | The name of the certificate. Must be unique across Wi-Fi profiles. |

## Example

```python
from adyen.models.file_4 import File4

file_4 = File4(
    data='data0',
    name='name0'
)
```

