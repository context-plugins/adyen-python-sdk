
# Sdk Ephem Pub Key 1

The `sdkEphemPubKey` value as received from the 3D Secure 2 SDK.

*This model accepts additional fields of type Any.*

## Structure

`SdkEphemPubKey1`

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

from adyen.models.sdk_ephem_pub_key_1 import SdkEphemPubKey1

sdk_ephem_pub_key_1 = SdkEphemPubKey1(
    crv='crv6',
    kty='kty6',
    x='x4',
    y='y2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

