
# Contact Details

## Structure

`ContactDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address`](../../doc/models/address.md) | Required | The address of the account holder. |
| `email` | `str` | Required | The email address of the account holder. |
| `phone` | [`Phone31`](../../doc/models/phone-31.md) | Required | The phone number of the account holder. |
| `web_address` | `str` | Optional | The URL of the account holder's website. |

## Example

```python
from adyen.models.address import Address
from adyen.models.contact_details import ContactDetails
from adyen.models.phone_31 import Phone31
from adyen.models.type_410_enum import Type410Enum

contact_details = ContactDetails(
    address=Address(
        city='city6',
        country='country0',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode8',
        street='street6',
        state_or_province='stateOrProvince4'
    ),
    email='email2',
    phone=Phone31(
        number='number8',
        mtype=Type410Enum.LANDLINE
    ),
    web_address='webAddress4'
)
```

