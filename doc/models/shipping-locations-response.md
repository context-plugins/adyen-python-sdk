
# Shipping Locations Response

*This model accepts additional fields of type Any.*

## Structure

`ShippingLocationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[ShippingLocation]`](../../doc/models/shipping-location.md) | Optional | Physical locations where orders can be shipped to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_6 import Address6
from adyen.models.contact import Contact
from adyen.models.shipping_location import ShippingLocation
from adyen.models.shipping_locations_response import ShippingLocationsResponse

shipping_locations_response = ShippingLocationsResponse(
    data=[
        ShippingLocation(
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
            id='id0',
            name='name0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ShippingLocation(
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
            id='id0',
            name='name0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ShippingLocation(
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
            id='id0',
            name='name0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

