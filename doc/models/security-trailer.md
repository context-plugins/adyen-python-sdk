
# Security Trailer

It contains information related to the security of the message.
SecurityTrailer as used by Adyen.

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

## Example

```python
from adyen.models.security_trailer import SecurityTrailer

security_trailer = SecurityTrailer(
    adyen_crypto_version=102,
    key_identifier='KeyIdentifier2',
    key_version=36,
    nonce='Nonce6',
    hmac='Hmac6'
)
```

