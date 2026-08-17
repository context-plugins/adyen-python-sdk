
# Shipping Location

## Structure

`ShippingLocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address21`](../../doc/models/address-21.md) | Optional | The address details of the shipping location. |
| `contact` | [`Contact1`](../../doc/models/contact-1.md) | Optional | The contact details for the shipping location. |
| `id` | `str` | Optional | The unique identifier of the shipping location, for use as `shippingLocationId` when creating an order. |
| `name` | `str` | Optional | The unique name of the shipping location. |

## Example

```python
from adyen.models.address_21 import Address21
from adyen.models.contact_1 import Contact1
from adyen.models.shipping_location import ShippingLocation

shipping_location = ShippingLocation(
    address=Address21(
        city='city6',
        company_name='companyName8',
        country='country0',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4'
    ),
    contact=Contact1(
        email='email4',
        first_name='firstName2',
        infix='infix6',
        last_name='lastName6',
        phone_number='phoneNumber2'
    ),
    id='id4',
    name='name4'
)
```

