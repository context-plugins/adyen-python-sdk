
# Sca Device 1

*This model accepts additional fields of type Any.*

## Structure

`ScaDevice1`

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

from adyen.models.sca_device_1 import ScaDevice1
from adyen.models.sca_device_type_1 import ScaDeviceType1

sca_device_1 = ScaDevice1(
    id='id0',
    name='name0',
    mtype=ScaDeviceType1.ANDROID,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

