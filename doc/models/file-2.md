
# File 2

For `eap` **tls**. The certificate chain for the terminals. All terminals in the same network will use the same EAP client certificate.

## Structure

`File2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `str` | Required | The certificate content converted to a Base64-encoded string. |
| `name` | `str` | Required | The name of the certificate. Must be unique across Wi-Fi profiles. |

## Example

```python
from adyen.models.file_2 import File2

file_2 = File2(
    data='data6',
    name='name6'
)
```

