
# Store Location

The address of the contact.

## Structure

`StoreLocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The name of the city. |
| `country` | `str` | Required | The two-letter country code in [ISO_3166-1_alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |
| `line_1` | `str` | Optional | The street address. |
| `line_2` | `str` | Optional | Second address line. |
| `line_3` | `str` | Optional | Third address line. |
| `postal_code` | `str` | Optional | The postal code. |
| `state_or_province` | `str` | Optional | The state or province code as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada.<br><br>Required for the following countries:<br><br>- Australia<br>- Brazil<br>- Canada<br>- India<br>- Mexico<br>- New Zealand<br>- United States |

## Example

```python
from adyen.models.store_location import StoreLocation

store_location = StoreLocation(
    country='country4',
    city='city0',
    line_1='line12',
    line_2='line24',
    line_3='line32',
    postal_code='postalCode2'
)
```

