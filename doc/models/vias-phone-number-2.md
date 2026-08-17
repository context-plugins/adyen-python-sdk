
# Vias Phone Number 2

The phone number of the entity.

## Structure

`ViasPhoneNumber2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `phone_country_code` | `str` | Optional | The two-character country code of the phone number.<br><br>> The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL'). |
| `phone_number` | `str` | Optional | The phone number.<br><br>> The inclusion of the phone number country code is not necessary. |
| `phone_type` | [`PhoneTypeEnum`](../../doc/models/phone-type-enum.md) | Optional | The type of the phone number.<br><br>> The following values are permitted: `Landline`, `Mobile`, `SIP`, `Fax`. |

## Example

```python
from adyen.models.phone_type_enum import PhoneTypeEnum
from adyen.models.vias_phone_number_2 import ViasPhoneNumber2

vias_phone_number_2 = ViasPhoneNumber2(
    phone_country_code='phoneCountryCode0',
    phone_number='phoneNumber2',
    phone_type=PhoneTypeEnum.FAX
)
```

