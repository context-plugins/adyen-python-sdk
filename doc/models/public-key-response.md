
# Public Key Response

## Structure

`PublicKeyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `public_key` | `str` | Required | The public key you need for encrypting a symmetric session key. |
| `public_key_expiry_date` | `str` | Required | The expiry date of the public key. |

## Example

```python
from adyen.models.public_key_response import PublicKeyResponse

public_key_response = PublicKeyResponse(
    public_key='publicKey2',
    public_key_expiry_date='publicKeyExpiryDate0'
)
```

