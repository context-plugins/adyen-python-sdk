
# Vias Phone Number 4

The phone number of the store.

## Structure

`ViasPhoneNumber4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `phone_country_code` | `str` | Optional | The two-character country code of the phone number.<br><br>> The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL'). |
| `phone_number` | `str` | Optional | The phone number.<br><br>> The inclusion of the phone number country code is not necessary. |
| `phone_type` | [`PhoneTypeEnum`](../../doc/models/phone-type-enum.md) | Optional | The type of the phone number.<br><br>> The following values are permitted: `Landline`, `Mobile`, `SIP`, `Fax`. |

## Example

```python
from adyen.models.phone_type_enum import PhoneTypeEnum
from adyen.models.vias_phone_number_4 import ViasPhoneNumber4

vias_phone_number_4 = ViasPhoneNumber4(
    phone_country_code='phoneCountryCode2',
    phone_number='phoneNumber6',
    phone_type=PhoneTypeEnum.FAX
)
```

