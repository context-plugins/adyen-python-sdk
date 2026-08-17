
# SDK Ephem Pub Key

The `sdkEphemPubKey` value as received from the 3D Secure 2 SDK.
Required for `deviceChannel` set to **app**.

## Structure

`SDKEphemPubKey`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `crv` | `str` | Optional | The `crv` value as received from the 3D Secure 2 SDK. |
| `kty` | `str` | Optional | The `kty` value as received from the 3D Secure 2 SDK. |
| `x` | `str` | Optional | The `x` value as received from the 3D Secure 2 SDK. |
| `y` | `str` | Optional | The `y` value as received from the 3D Secure 2 SDK. |

## Example

```python
from adyen.models.sdk_ephem_pub_key import SDKEphemPubKey

sdk_ephem_pub_key = SDKEphemPubKey(
    crv='crv2',
    kty='kty2',
    x='x0',
    y='y8'
)
```

