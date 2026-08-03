
# Address 13

The address of the store.

*This model accepts additional fields of type Any.*

## Structure

`Address13`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | - |
| `country_code` | `str` | Optional | - |
| `postal_code` | `str` | Optional | - |
| `state_or_province` | `str` | Optional | - |
| `street_address` | `str` | Optional | - |
| `street_address_2` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_13 import Address13

address_13 = Address13(
    city='city6',
    country_code='countryCode0',
    postal_code='postalCode4',
    state_or_province='stateOrProvince8',
    street_address='streetAddress6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

