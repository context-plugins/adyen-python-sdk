
# Phone Info

*This model accepts additional fields of type Any.*

## Structure

`PhoneInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hashed_number` | `str` | Optional | The hashed value of the phone number used to provision the network token. |
| `last_four_digits` | `str` | Optional | The last four digits of the phone number used to provision the network token. |
| `number` | `str` | Optional | The full phone number of the device used to provision the network token. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.phone_info import PhoneInfo

phone_info = PhoneInfo(
    hashed_number='hashedNumber8',
    last_four_digits='lastFourDigits2',
    number='number2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

