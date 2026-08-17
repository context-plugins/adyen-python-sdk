
# Bulk Address 1

Overrides the shipment bulk address defined in the card configuration profile.

## Structure

`BulkAddress1`

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

## Example

```python
from adyen.models.bulk_address_1 import BulkAddress1

bulk_address_1 = BulkAddress1(
    country='country6',
    city='city2',
    company='company2',
    email='email4',
    house_number_or_name='houseNumberOrName0',
    line_1='line14'
)
```

