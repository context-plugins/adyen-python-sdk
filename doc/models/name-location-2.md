
# Name Location 2

Contains the name and location of the merchant.

## Structure

`NameLocation2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The city where the merchant is located. |
| `country` | `str` | Optional | The country where the merchant is located in [three-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) format. |
| `country_of_origin` | `str` | Optional | The home country in [three-digit country code](https://en.wikipedia.org/wiki/ISO_3166-1_numeric) format, used for government-controlled merchants such as embassies. |
| `name` | `str` | Optional | The name of the merchant's shop or service. |
| `raw_data` | `str` | Optional | The raw data. |
| `state` | `str` | Optional | The state where the merchant is located. |

## Example

```python
from adyen.models.name_location_2 import NameLocation2

name_location_2 = NameLocation2(
    city='city4',
    country='country8',
    country_of_origin='countryOfOrigin0',
    name='name4',
    raw_data='rawData0'
)
```

