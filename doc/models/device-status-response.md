
# Device Status Response

*This model accepts additional fields of type Any.*

## Structure

`DeviceStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Optional | The unique identification of the device.<br>This can be a payment terminal ID in the format _[terminal model]-[serial number]_ (for example, P400‑123456789), or an SDK installation ID as used in Mobile solutions. |
| `status` | [`DeviceStatus1`](../../doc/models/device-status-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device_status_1 import DeviceStatus1
from adyen.models.device_status_response import DeviceStatusResponse

device_status_response = DeviceStatusResponse(
    device_id='deviceId4',
    status=DeviceStatus1.ONLINE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

