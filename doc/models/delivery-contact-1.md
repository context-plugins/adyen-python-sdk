
# Delivery Contact 1

The delivery contact (name and address) for physical card delivery.

*This model accepts additional fields of type Any.*

## Structure

`DeliveryContact1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address15`](../../doc/models/address-15.md) | Required | - |
| `company` | `str` | Optional | The company name of the contact. |
| `email` | `str` | Optional | The email address of the contact. |
| `full_phone_number` | `str` | Optional | The full phone number of the contact provided as a single string. It will be handled as a landline phone.<br>**Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344" |
| `name` | [`Name5`](../../doc/models/name-5.md) | Required | - |
| `phone_number` | [`PhoneNumber3`](../../doc/models/phone-number-3.md) | Optional | - |
| `web_address` | `str` | Optional | The URL of the contact's website. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_15 import Address15
from adyen.models.delivery_contact_1 import DeliveryContact1
from adyen.models.name_5 import Name5
from adyen.models.phone_number_3 import PhoneNumber3
from adyen.models.phone_type import PhoneType

delivery_contact_1 = DeliveryContact1(
    address=Address15(
        country='country0',
        city='city6',
        line_1='line18',
        line_2='line20',
        line_3='line38',
        postal_code='postalCode8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    name=Name5(
        first_name='firstName4',
        last_name='lastName4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    company='company0',
    email='email6',
    full_phone_number='fullPhoneNumber4',
    phone_number=PhoneNumber3(
        phone_country_code='phoneCountryCode8',
        phone_number='phoneNumber0',
        phone_type=PhoneType.FAX,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    web_address='webAddress0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

