
# Delivery Address 5

The delivery address for this order.

## Structure

`DeliveryAddress5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Required | The name of the city. Maximum length: 3000 characters.<br><br>**Constraints**: *Maximum Length*: `3000` |
| `country` | `str` | Required | The two-character ISO-3166-1 alpha-2 country code. For example, **US**.<br><br>> If you don't know the country or are not collecting the country from the shopper, provide `country` as `ZZ`. |
| `first_name` | `str` | Optional | - |
| `house_number_or_name` | `str` | Required | The number or name of the house. Maximum length: 3000 characters.<br><br>**Constraints**: *Maximum Length*: `3000` |
| `last_name` | `str` | Optional | - |
| `postal_code` | `str` | Required | A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.<br><br>**Constraints**: *Maximum Length*: `10` |
| `state_or_province` | `str` | Optional | The two-character ISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada.<br><br>> Required for the US and Canada.<br><br>**Constraints**: *Maximum Length*: `3` |
| `street` | `str` | Required | The name of the street. Maximum length: 3000 characters.<br><br>> The house number should not be included in this field; it should be separately provided via `houseNumberOrName`.<br><br>**Constraints**: *Maximum Length*: `3000` |

## Example

```python
from adyen.models.delivery_address_5 import DeliveryAddress5

delivery_address_5 = DeliveryAddress5(
    city='city0',
    country='country4',
    house_number_or_name='houseNumberOrName8',
    postal_code='postalCode8',
    street='street0',
    first_name='firstName4',
    last_name='lastName4',
    state_or_province='stateOrProvince8'
)
```

