
# Vias Address 5

The address of the entity.

*This model accepts additional fields of type Any.*

## Structure

`ViasAddress5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The name of the city. Required if the `houseNumberOrName`, `street`, `postalCode`, or `stateOrProvince` are provided. |
| `country` | `str` | Required | The two-character country code of the address in ISO-3166-1 alpha-2 format. For example, **NL**. |
| `house_number_or_name` | `str` | Optional | The number or name of the house. |
| `postal_code` | `str` | Optional | The postal code. Required if the `houseNumberOrName`, `street`, `city`, or `stateOrProvince` are provided.<br><br>Maximum length:<br><br>* 5 digits for addresses in the US.<br><br>* 10 characters for all other countries. |
| `state_or_province` | `str` | Optional | The abbreviation of the state or province. Required if the `houseNumberOrName`, `street`, `city`, or `postalCode` are provided.<br><br>Maximum length:<br><br>* 2 characters for addresses in the US or Canada.<br><br>* 3 characters for all other countries. |
| `street` | `str` | Optional | The name of the street. Required if the `houseNumberOrName`, `city`, `postalCode`, or `stateOrProvince` are provided. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.vias_address_5 import ViasAddress5

vias_address_5 = ViasAddress5(
    country='country2',
    city='city2',
    house_number_or_name='houseNumberOrName6',
    postal_code='postalCode0',
    state_or_province='stateOrProvince6',
    street='street8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

