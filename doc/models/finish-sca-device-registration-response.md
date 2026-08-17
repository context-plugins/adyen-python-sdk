
# Finish Sca Device Registration Response

## Structure

`FinishScaDeviceRegistrationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sca_device` | [`ScaDevice`](../../doc/models/sca-device.md) | Optional | A resource that contains information about a device, including its unique ID, name, and type. |

## Example

```python
from adyen.models.finish_sca_device_registration_response import FinishScaDeviceRegistrationResponse
from adyen.models.sca_device import ScaDevice
from adyen.models.sca_device_type_1_enum import ScaDeviceType1Enum

finish_sca_device_registration_response = FinishScaDeviceRegistrationResponse(
    sca_device=ScaDevice(
        id='id2',
        name='name2',
        mtype=ScaDeviceType1Enum.BROWSER
    )
)
```

