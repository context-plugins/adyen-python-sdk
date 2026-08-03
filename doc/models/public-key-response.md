
# Public Key Response

*This model accepts additional fields of type Any.*

## Structure

`PublicKeyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `public_key` | `str` | Required | The public key you need for encrypting a symmetric session key. |
| `public_key_expiry_date` | `str` | Required | The expiry date of the public key. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.public_key_response import PublicKeyResponse

public_key_response = PublicKeyResponse(
    public_key='publicKey2',
    public_key_expiry_date='publicKeyExpiryDate0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

