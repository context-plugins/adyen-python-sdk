
# Address 14

The address of the store.

## Structure

`Address14`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | - |
| `country_code` | `str` | Optional | - |
| `postal_code` | `str` | Optional | - |
| `state_or_province` | `str` | Optional | - |
| `street_address` | `str` | Optional | - |
| `street_address_2` | `str` | Optional | - |

## Example

```python
from adyen.models.address_14 import Address14

address_14 = Address14(
    city='city2',
    country_code='countryCode2',
    postal_code='postalCode4',
    state_or_province='stateOrProvince0',
    street_address='streetAddress2'
)
```

