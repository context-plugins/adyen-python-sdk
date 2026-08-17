
# File

## Structure

`File`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `str` | Required | The certificate content converted to a Base64-encoded string. |
| `name` | `str` | Required | The name of the certificate. Must be unique across Wi-Fi profiles. |

## Example

```python
from adyen.models.file import File

file = File(
    data='data0',
    name='name0'
)
```

