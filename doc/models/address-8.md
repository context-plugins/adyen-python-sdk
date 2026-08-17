
# Address 8

## Structure

`Address8`

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
from adyen.models.address_8 import Address8

address_8 = Address8(
    city='city6',
    country_code='countryCode8',
    postal_code='postalCode8',
    state_or_province='stateOrProvince4',
    street_address='streetAddress6'
)
```

