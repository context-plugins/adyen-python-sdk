
# Shipping Locations Response

## Structure

`ShippingLocationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[ShippingLocation]`](../../doc/models/shipping-location.md) | Optional | Physical locations where orders can be shipped to. |

## Example

```python
from adyen.models.address_21 import Address21
from adyen.models.contact_1 import Contact1
from adyen.models.shipping_location import ShippingLocation
from adyen.models.shipping_locations_response import ShippingLocationsResponse

shipping_locations_response = ShippingLocationsResponse(
    data=[
        ShippingLocation(
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
            id='id0',
            name='name0'
        ),
        ShippingLocation(
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
            id='id0',
            name='name0'
        ),
        ShippingLocation(
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
            id='id0',
            name='name0'
        )
    ]
)
```

