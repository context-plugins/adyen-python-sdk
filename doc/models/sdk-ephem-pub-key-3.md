
# Sdk Ephem Pub Key 3

*This model accepts additional fields of type Any.*

## Structure

`SdkEphemPubKey3`

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

from adyen.models.sdk_ephem_pub_key_3 import SdkEphemPubKey3

sdk_ephem_pub_key_3 = SdkEphemPubKey3(
    crv='crv4',
    kty='kty4',
    x='x2',
    y='y0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

