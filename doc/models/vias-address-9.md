
# Vias Address 9

The address of the account holder.

## Structure

`ViasAddress9`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The name of the city. Required if the `houseNumberOrName`, `street`, `postalCode`, or `stateOrProvince` are provided. |
| `country` | `str` | Required | The two-character country code of the address in ISO-3166-1 alpha-2 format. For example, **NL**. |
| `house_number_or_name` | `str` | Optional | The number or name of the house. |
| `postal_code` | `str` | Optional | The postal code. Required if the `houseNumberOrName`, `street`, `city`, or `stateOrProvince` are provided.<br><br>Maximum length:<br><br>* 5 digits for addresses in the US.<br><br>* 10 characters for all other countries. |
| `state_or_province` | `str` | Optional | The abbreviation of the state or province. Required if the `houseNumberOrName`, `street`, `city`, or `postalCode` are provided.<br><br>Maximum length:<br><br>* 2 characters for addresses in the US or Canada.<br><br>* 3 characters for all other countries. |
| `street` | `str` | Optional | The name of the street. Required if the `houseNumberOrName`, `city`, `postalCode`, or `stateOrProvince` are provided. |

## Example

```python
from adyen.models.vias_address_9 import ViasAddress9

vias_address_9 = ViasAddress9(
    country='country0',
    city='city6',
    house_number_or_name='houseNumberOrName4',
    postal_code='postalCode8',
    state_or_province='stateOrProvince4',
    street='street6'
)
```

