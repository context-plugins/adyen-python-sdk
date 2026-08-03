
# Address 11

The residential address of the individual.

*This model accepts additional fields of type Any.*

## Structure

`Address11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The name of the city. Required if `stateOrProvince` is provided.<br><br>If you specify the city, you must also send `postalCode` and `street`. |
| `country` | `str` | Required | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
| `postal_code` | `str` | Optional | The postal code. Required if `stateOrProvince` and/or `city` is provided.<br><br>When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
| `state_or_province` | `str` | Optional | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.<br><br>If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
| `street` | `str` | Optional | The name of the street, and the house or building number. Required if `stateOrProvince` and/or `city` is provided. |
| `street_2` | `str` | Optional | The apartment, unit, or suite number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_11 import Address11

address_11 = Address11(
    country='country8',
    city='city4',
    postal_code='postalCode4',
    state_or_province='stateOrProvince2',
    street='street4',
    street_2='street20',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

