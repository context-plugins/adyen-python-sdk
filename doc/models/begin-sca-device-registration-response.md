
# Begin Sca Device Registration Response

*This model accepts additional fields of type Any.*

## Structure

`BeginScaDeviceRegistrationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sca_device` | [`ScaDevice1`](../../doc/models/sca-device-1.md) | Optional | - |
| `sdk_input` | `str` | Optional | A string that you must pass to the authentication SDK to continue with the registration process.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.begin_sca_device_registration_response import BeginScaDeviceRegistrationResponse
from adyen.models.sca_device_1 import ScaDevice1
from adyen.models.sca_device_type_1 import ScaDeviceType1

begin_sca_device_registration_response = BeginScaDeviceRegistrationResponse(
    sca_device=ScaDevice1(
        id='id2',
        name='name2',
        mtype=ScaDeviceType1.BROWSER,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    sdk_input='sdkInput8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

