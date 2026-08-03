
# Shipping Location

*This model accepts additional fields of type Any.*

## Structure

`ShippingLocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address6`](../../doc/models/address-6.md) | Optional | - |
| `contact` | [`Contact`](../../doc/models/contact.md) | Optional | - |
| `id` | `str` | Optional | The unique identifier of the shipping location, for use as `shippingLocationId` when creating an order. |
| `name` | `str` | Optional | The unique name of the shipping location. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_6 import Address6
from adyen.models.contact import Contact
from adyen.models.shipping_location import ShippingLocation

shipping_location = ShippingLocation(
    address=Address6(
        city='city6',
        company_name='companyName8',
        country='country0',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    contact=Contact(
        email='email4',
        first_name='firstName2',
        infix='infix6',
        last_name='lastName6',
        phone_number='phoneNumber2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    id='id4',
    name='name4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

