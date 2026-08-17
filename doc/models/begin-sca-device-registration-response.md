
# Begin Sca Device Registration Response

## Structure

`BeginScaDeviceRegistrationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sca_device` | [`ScaDevice`](../../doc/models/sca-device.md) | Optional | A resource that contains information about a device, including its unique ID, name, and type. |
| `sdk_input` | `str` | Optional | A string that you must pass to the authentication SDK to continue with the registration process.<br><br>**Constraints**: *Maximum Length*: `20000` |

## Example

```python
from adyen.models.begin_sca_device_registration_response import BeginScaDeviceRegistrationResponse
from adyen.models.sca_device import ScaDevice
from adyen.models.sca_device_type_1_enum import ScaDeviceType1Enum

begin_sca_device_registration_response = BeginScaDeviceRegistrationResponse(
    sca_device=ScaDevice(
        id='id2',
        name='name2',
        mtype=ScaDeviceType1Enum.BROWSER
    ),
    sdk_input='sdkInput8'
)
```

