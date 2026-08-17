
# Phone Info

## Structure

`PhoneInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hashed_number` | `str` | Optional | The hashed value of the phone number used to provision the network token. |
| `last_four_digits` | `str` | Optional | The last four digits of the phone number used to provision the network token. |
| `number` | `str` | Optional | The full phone number of the device used to provision the network token. |

## Example

```python
from adyen.models.phone_info import PhoneInfo

phone_info = PhoneInfo(
    hashed_number='hashedNumber8',
    last_four_digits='lastFourDigits2',
    number='number2'
)
```

