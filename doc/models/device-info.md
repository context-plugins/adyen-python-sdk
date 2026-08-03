
# Device Info

*This model accepts additional fields of type Any.*

## Structure

`DeviceInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `form_factor` | `str` | Optional | The type of device used to provision the network token. |
| `os_name` | `str` | Optional | The operating system of the device used to provision the network token. |
| `phone` | [`PhoneInfo`](../../doc/models/phone-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device_info import DeviceInfo
from adyen.models.phone_info import PhoneInfo

device_info = DeviceInfo(
    form_factor='formFactor6',
    os_name='osName6',
    phone=PhoneInfo(
        hashed_number='hashedNumber2',
        last_four_digits='lastFourDigits8',
        number='number8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

