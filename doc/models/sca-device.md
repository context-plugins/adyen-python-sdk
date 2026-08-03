
# Sca Device

A resource that contains information about a device, including its unique ID, name, and type.

*This model accepts additional fields of type Any.*

## Structure

`ScaDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The unique identifier of the SCA device you are registering. |
| `name` | `str` | Required | The name of the SCA device that you are registering. You can use it to help your users identify the device.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `64` |
| `mtype` | [`ScaDeviceType1`](../../doc/models/sca-device-type-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sca_device import ScaDevice
from adyen.models.sca_device_type_1 import ScaDeviceType1

sca_device = ScaDevice(
    id='id2',
    name='name2',
    mtype=ScaDeviceType1.ANDROID,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

