
# Address 4

## Structure

`Address4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The name of the city. |
| `company_name` | `str` | Optional | The name of the company. |
| `country` | `str` | Optional | The two-letter country code, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |
| `postal_code` | `str` | Optional | The postal code. |
| `state_or_province` | `str` | Optional | The state or province as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada.<br><br>Applicable for the following countries:<br><br>- Australia<br>- Brazil<br>- Canada<br>- India<br>- Mexico<br>- New Zealand<br>- United States |
| `street_address` | `str` | Optional | The name of the street, and the house or building number. |
| `street_address_2` | `str` | Optional | Additional address details, if any. |

## Example

```python
from adyen.models.address_4 import Address4

address_4 = Address4(
    city='city0',
    company_name='companyName2',
    country='country4',
    postal_code='postalCode8',
    state_or_province='stateOrProvince8'
)
```

