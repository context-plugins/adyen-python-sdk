
# Phone Info 2

The information about the phone number of the device used to provision the the network token. This object is conditionally returned and is available for up to 24 hours after the provisioning request (access to this field requires a specific user role, please contact your Adyen representative to request permission).

## Structure

`PhoneInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hashed_number` | `str` | Optional | The hashed value of the phone number used to provision the network token. |
| `last_four_digits` | `str` | Optional | The last four digits of the phone number used to provision the network token. |
| `number` | `str` | Optional | The full phone number of the device used to provision the network token. |

## Example

```python
from adyen.models.phone_info_2 import PhoneInfo2

phone_info_2 = PhoneInfo2(
    hashed_number='hashedNumber2',
    last_four_digits='lastFourDigits8',
    number='number2'
)
```

