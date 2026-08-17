
# Generate Hmac Key Response

## Structure

`GenerateHmacKeyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hmac_key` | `str` | Required | The HMAC key generated for this webhook. |

## Example

```python
from adyen.models.generate_hmac_key_response import GenerateHmacKeyResponse

generate_hmac_key_response = GenerateHmacKeyResponse(
    hmac_key='hmacKey2'
)
```

