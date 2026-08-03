
# Finish Sca Device Registration Response

*This model accepts additional fields of type Any.*

## Structure

`FinishScaDeviceRegistrationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sca_device` | [`ScaDevice1`](../../doc/models/sca-device-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.finish_sca_device_registration_response import FinishScaDeviceRegistrationResponse
from adyen.models.sca_device_1 import ScaDevice1
from adyen.models.sca_device_type_1 import ScaDeviceType1

finish_sca_device_registration_response = FinishScaDeviceRegistrationResponse(
    sca_device=ScaDevice1(
        id='id2',
        name='name2',
        mtype=ScaDeviceType1.BROWSER,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

