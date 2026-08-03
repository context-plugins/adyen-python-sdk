
# Billing Address

*This model accepts additional fields of type Any.*

## Structure

`BillingAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Required | The name of the city. Maximum length: 3000 characters.<br><br>**Constraints**: *Maximum Length*: `3000` |
| `country` | `str` | Required | The two-character ISO-3166-1 alpha-2 country code. For example, **US**.<br><br>> If you don't know the country or are not collecting the country from the shopper, provide `country` as `ZZ`. |
| `house_number_or_name` | `str` | Required | The number or name of the house. Maximum length: 3000 characters.<br><br>**Constraints**: *Maximum Length*: `3000` |
| `postal_code` | `str` | Required | A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.<br><br>**Constraints**: *Maximum Length*: `10` |
| `state_or_province` | `str` | Optional | The two-character ISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada.<br><br>> Required for the US and Canada.<br><br>**Constraints**: *Maximum Length*: `3` |
| `street` | `str` | Required | The name of the street. Maximum length: 3000 characters.<br><br>> The house number should not be included in this field; it should be separately provided via `houseNumberOrName`.<br><br>**Constraints**: *Maximum Length*: `3000` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.billing_address import BillingAddress

billing_address = BillingAddress(
    city='city2',
    country='country2',
    house_number_or_name='houseNumberOrName6',
    postal_code='postalCode0',
    street='street8',
    state_or_province='stateOrProvince6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

