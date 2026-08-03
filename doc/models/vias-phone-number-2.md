
# Vias Phone Number 2

The phone number of the entity.

*This model accepts additional fields of type Any.*

## Structure

`ViasPhoneNumber2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `phone_country_code` | `str` | Optional | The two-character country code of the phone number.<br><br>> The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL'). |
| `phone_number` | `str` | Optional | The phone number.<br><br>> The inclusion of the phone number country code is not necessary. |
| `phone_type` | [`PhoneType`](../../doc/models/phone-type.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.phone_type import PhoneType
from adyen.models.vias_phone_number_2 import ViasPhoneNumber2

vias_phone_number_2 = ViasPhoneNumber2(
    phone_country_code='phoneCountryCode0',
    phone_number='phoneNumber2',
    phone_type=PhoneType.FAX,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

