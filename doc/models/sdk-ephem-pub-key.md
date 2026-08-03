
# Sdk Ephem Pub Key

The `sdkEphemPubKey` value as received from the 3D Secure 2 SDK.
Required for `deviceChannel` set to **app**.

*This model accepts additional fields of type Any.*

## Structure

`SdkEphemPubKey`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `crv` | `str` | Optional | The `crv` value as received from the 3D Secure 2 SDK. |
| `kty` | `str` | Optional | The `kty` value as received from the 3D Secure 2 SDK. |
| `x` | `str` | Optional | The `x` value as received from the 3D Secure 2 SDK. |
| `y` | `str` | Optional | The `y` value as received from the 3D Secure 2 SDK. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sdk_ephem_pub_key import SdkEphemPubKey

sdk_ephem_pub_key = SdkEphemPubKey(
    crv='crv2',
    kty='kty2',
    x='x0',
    y='y8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

