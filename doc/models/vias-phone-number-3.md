
# Vias Phone Number 3

The phone number of the account holder.

> Required if a `fullPhoneNumber` is not provided.

## Structure

`ViasPhoneNumber3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `phone_country_code` | `str` | Optional | The two-character country code of the phone number.<br><br>> The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL'). |
| `phone_number` | `str` | Optional | The phone number.<br><br>> The inclusion of the phone number country code is not necessary. |
| `phone_type` | [`PhoneTypeEnum`](../../doc/models/phone-type-enum.md) | Optional | The type of the phone number.<br><br>> The following values are permitted: `Landline`, `Mobile`, `SIP`, `Fax`. |

## Example

```python
from adyen.models.phone_type_enum import PhoneTypeEnum
from adyen.models.vias_phone_number_3 import ViasPhoneNumber3

vias_phone_number_3 = ViasPhoneNumber3(
    phone_country_code='phoneCountryCode6',
    phone_number='phoneNumber8',
    phone_type=PhoneTypeEnum.MOBILE
)
```

