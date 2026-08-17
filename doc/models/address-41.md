
# Address 41

The business address. Required if the principal place of business is different from the `registeredAddress`.

## Structure

`Address41`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The name of the city. Required if `stateOrProvince` is provided.<br><br>If you specify the city, you must also send `postalCode` and `street`. |
| `country` | `str` | Required | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
| `postal_code` | `str` | Optional | The postal code. Required if `stateOrProvince` and/or `city` is provided.<br><br>When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
| `state_or_province` | `str` | Optional | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.<br><br>If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
| `street` | `str` | Optional | The name of the street, and the house or building number. Required if `stateOrProvince` and/or `city` is provided. |
| `street_2` | `str` | Optional | The apartment, unit, or suite number. |

## Example

```python
from adyen.models.address_41 import Address41

address_41 = Address41(
    country='country6',
    city='city8',
    postal_code='postalCode6',
    state_or_province='stateOrProvince0',
    street='street2',
    street_2='street22'
)
```

