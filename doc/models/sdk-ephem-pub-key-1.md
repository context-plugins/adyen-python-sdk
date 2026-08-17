
# SDK Ephem Pub Key 1

The `sdkEphemPubKey` value as received from the 3D Secure 2 SDK.

## Structure

`SDKEphemPubKey1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `crv` | `str` | Optional | The `crv` value as received from the 3D Secure 2 SDK. |
| `kty` | `str` | Optional | The `kty` value as received from the 3D Secure 2 SDK. |
| `x` | `str` | Optional | The `x` value as received from the 3D Secure 2 SDK. |
| `y` | `str` | Optional | The `y` value as received from the 3D Secure 2 SDK. |

## Example

```python
from adyen.models.sdk_ephem_pub_key_1 import SDKEphemPubKey1

sdk_ephem_pub_key_1 = SDKEphemPubKey1(
    crv='crv6',
    kty='kty6',
    x='x4',
    y='y2'
)
```

