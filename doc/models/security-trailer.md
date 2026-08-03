
# Security Trailer

It contains information related to the security of the message.
SecurityTrailer as used by Adyen.

*This model accepts additional fields of type Any.*

## Structure

`SecurityTrailer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adyen_crypto_version` | `int` | Required | - |
| `key_identifier` | `str` | Required | **Constraints**: *Pattern*: `^.+$` |
| `key_version` | `int` | Required | - |
| `nonce` | `str` | Required | **Constraints**: *Pattern*: `^.+$` |
| `hmac` | `str` | Required | **Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.security_trailer import SecurityTrailer

security_trailer = SecurityTrailer(
    adyen_crypto_version=102,
    key_identifier='KeyIdentifier2',
    key_version=36,
    nonce='Nonce6',
    hmac='Hmac6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

