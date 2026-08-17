
# Store Location 1

The address of the store.

## Structure

`StoreLocation1`

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
from adyen.models.store_location_1 import StoreLocation1

store_location_1 = StoreLocation1(
    country='country6',
    city='city8',
    line_1='line14',
    line_2='line26',
    line_3='line34',
    postal_code='postalCode6'
)
```

