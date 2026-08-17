
# Address 5

The billing address associated with the stored payment method.

## Structure

`Address5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Required | The name of the city. Maximum length: 3000 characters.<br><br>**Constraints**: *Maximum Length*: `3000` |
| `country` | `str` | Required | The two-character ISO-3166-1 alpha-2 country code. For example, **US**.<br><br>> If you don't know the country or are not collecting the country from the shopper, provide `country` as `ZZ`. |
| `house_number_or_name` | `str` | Required | The number or name of the house. Maximum length: 3000 characters.<br><br>**Constraints**: *Maximum Length*: `3000` |
| `postal_code` | `str` | Required | A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries. |
| `state_or_province` | `str` | Optional | The two-character ISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada.<br><br>> Required for the US and Canada. |
| `street` | `str` | Required | The name of the street. Maximum length: 3000 characters.<br><br>> The house number should not be included in this field; it should be separately provided via `houseNumberOrName`.<br><br>**Constraints**: *Maximum Length*: `3000` |

## Example

```python
from adyen.models.address_5 import Address5

address_5 = Address5(
    city='city0',
    country='country4',
    house_number_or_name='houseNumberOrName8',
    postal_code='postalCode8',
    street='street0',
    state_or_province='stateOrProvince8'
)
```

