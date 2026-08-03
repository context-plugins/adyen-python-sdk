
# Bulk Address

*This model accepts additional fields of type Any.*

## Structure

`BulkAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The name of the city. |
| `company` | `str` | Optional | The name of the company. |
| `country` | `str` | Required | The two-character ISO-3166-1 alpha-2 country code. For example, **US**. |
| `email` | `str` | Optional | The email address. |
| `house_number_or_name` | `str` | Optional | The house number or name. |
| `line_1` | `str` | Optional | The name of the street and the number of the building.<br><br>For example: **Simon Carmiggeltstraat 6-50**. |
| `line_2` | `str` | Optional | Additional information about the delivery address. For example, an apartment number. |
| `line_3` | `str` | Optional | Additional information about the delivery address. |
| `mobile` | `str` | Optional | The full telephone number. |
| `name` | `str` | Optional | The recipient’s name (person or contact), for example ‘John Doe’. |
| `postal_code` | `str` | Optional | The postal code.<br><br>Maximum length:<br><br>* 5 digits for addresses in the US.<br><br>* 10 characters for all other countries. |
| `state_or_province` | `str` | Optional | The two-letter ISO 3166-2 state or province code.<br><br>Maximum length: 2 characters for addresses in the US. |
| `street` | `str` | Optional | The streetname of the house. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bulk_address import BulkAddress

bulk_address = BulkAddress(
    country='country0',
    city='city6',
    company='company6',
    email='email0',
    house_number_or_name='houseNumberOrName4',
    line_1='line18',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

