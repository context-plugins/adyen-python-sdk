
# Contact Details

*This model accepts additional fields of type Any.*

## Structure

`ContactDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address112`](../../doc/models/address-112.md) | Required | - |
| `email` | `str` | Required | The email address of the account holder. |
| `phone` | [`Phone`](../../doc/models/phone.md) | Required | - |
| `web_address` | `str` | Optional | The URL of the account holder's website. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_112 import Address112
from adyen.models.contact_details import ContactDetails
from adyen.models.phone import Phone
from adyen.models.type_4 import Type4

contact_details = ContactDetails(
    address=Address112(
        city='city6',
        country='country0',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode8',
        street='street6',
        state_or_province='stateOrProvince4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    email='email2',
    phone=Phone(
        number='number8',
        mtype=Type4.LANDLINE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    web_address='webAddress4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

