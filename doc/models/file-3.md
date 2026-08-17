
# File 3

For `eap` **tls**. The RSA private key for the client. Include the lines BEGIN RSA PRIVATE KEY and END RSA PRIVATE KEY.

## Structure

`File3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `str` | Required | The certificate content converted to a Base64-encoded string. |
| `name` | `str` | Required | The name of the certificate. Must be unique across Wi-Fi profiles. |

## Example

```python
from adyen.models.file_3 import File3

file_3 = File3(
    data='data8',
    name='name8'
)
```

