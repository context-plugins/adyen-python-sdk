
# Device Info 1

Contains information about the device used to provision the network token.

## Structure

`DeviceInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `form_factor` | `str` | Optional | The type of device used to provision the network token. |
| `os_name` | `str` | Optional | The operating system of the device used to provision the network token. |
| `phone` | [`PhoneInfo2`](../../doc/models/phone-info-2.md) | Optional | The information about the phone number of the device used to provision the the network token. This object is conditionally returned and is available for up to 24 hours after the provisioning request (access to this field requires a specific user role, please contact your Adyen representative to request permission). |

## Example

```python
from adyen.models.device_info_1 import DeviceInfo1
from adyen.models.phone_info_2 import PhoneInfo2

device_info_1 = DeviceInfo1(
    form_factor='formFactor4',
    os_name='osName6',
    phone=PhoneInfo2(
        hashed_number='hashedNumber2',
        last_four_digits='lastFourDigits8',
        number='number8'
    )
)
```

