
# Delivery Contact 1

The delivery contact (name and address) for physical card delivery.

## Structure

`DeliveryContact1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`StoreLocation`](../../doc/models/store-location.md) | Required | The address of the contact. |
| `company` | `str` | Optional | The company name of the contact. |
| `email` | `str` | Optional | The email address of the contact. |
| `full_phone_number` | `str` | Optional | The full phone number of the contact provided as a single string. It will be handled as a landline phone.<br>**Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344" |
| `name` | [`Name`](../../doc/models/name.md) | Required | The name of the contact. |
| `phone_number` | [`ViasPhoneNumber`](../../doc/models/vias-phone-number.md) | Optional | The phone number of the contact. |
| `web_address` | `str` | Optional | The URL of the contact's website. |

## Example

```python
from adyen.models.delivery_contact_1 import DeliveryContact1
from adyen.models.name import Name
from adyen.models.phone_type_enum import PhoneTypeEnum
from adyen.models.store_location import StoreLocation
from adyen.models.vias_phone_number import ViasPhoneNumber

delivery_contact_1 = DeliveryContact1(
    address=StoreLocation(
        country='country0',
        city='city6',
        line_1='line18',
        line_2='line20',
        line_3='line38',
        postal_code='postalCode8'
    ),
    name=Name(
        first_name='firstName4',
        last_name='lastName4'
    ),
    company='company0',
    email='email6',
    full_phone_number='fullPhoneNumber4',
    phone_number=ViasPhoneNumber(
        phone_country_code='phoneCountryCode8',
        phone_number='phoneNumber0',
        phone_type=PhoneTypeEnum.FAX
    ),
    web_address='webAddress0'
)
```

