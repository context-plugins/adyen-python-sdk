
# Connected Devices Response

*This model accepts additional fields of type Any.*

## Structure

`ConnectedDevicesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unique_device_ids` | `List[str]` | Optional | A list of the unique IDs of the devices that have an active cloud connection.<br>The IDs are payment terminal IDs in the format _[terminal model]-[serial number]_ (for example, P400‑123456789), or SDK installation IDs as used in Mobile solutions. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.connected_devices_response import ConnectedDevicesResponse

connected_devices_response = ConnectedDevicesResponse(
    unique_device_ids=[
        'uniqueDeviceIds9',
        'uniqueDeviceIds0'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

