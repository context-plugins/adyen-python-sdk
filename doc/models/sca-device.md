
# Sca Device

A resource that contains information about a device, including its unique ID, name, and type.

## Structure

`ScaDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The unique identifier of the SCA device you are registering. |
| `name` | `str` | Required | The name of the SCA device that you are registering. You can use it to help your users identify the device.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `64` |
| `mtype` | [`ScaDeviceType1Enum`](../../doc/models/sca-device-type-1-enum.md) | Required | Type of device registered.<br><br>Possible values: **ios**, **android**, **browser**. |

## Example

```python
from adyen.models.sca_device import ScaDevice
from adyen.models.sca_device_type_1_enum import ScaDeviceType1Enum

sca_device = ScaDevice(
    id='id2',
    name='name2',
    mtype=ScaDeviceType1Enum.ANDROID
)
```

