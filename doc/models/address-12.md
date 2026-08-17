
# Address 12

The address of the bank account or card owner.

## Structure

`Address12`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The name of the city.<br><br>Supported characters: **[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ \|** and Space.<br><br>> Required when the `category` is **card**.<br><br>**Constraints**: *Minimum Length*: `3` |
| `country` | `str` | Required | The two-character ISO 3166-1 alpha-2 country code. For example, **US**, **NL**, or **GB**. |
| `line_1` | `str` | Optional | The first line of the street address.<br><br>Supported characters: **[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ \|** and Space.<br><br>> Required when the `category` is **card**. |
| `line_2` | `str` | Optional | The second line of the street address.<br><br>Supported characters: **[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ \|** and Space.<br><br>> Required when the `category` is **card**. |
| `postal_code` | `str` | Optional | The postal code.<br>Maximum length:<br><br>* 5 digits for an address in the US.<br>* 10 characters for an address in all other countries.<br><br>Supported characters: **[a-z] [A-Z] [0-9]** and Space.<br><br>> Required for addresses in the US.<br><br>**Constraints**: *Minimum Length*: `3` |
| `state_or_province` | `str` | Optional | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada.<br><br>> Required for the US and Canada. |

## Example

```python
from adyen.models.address_12 import Address12

address_12 = Address12(
    country='country2',
    city='city2',
    line_1='line10',
    line_2='line22',
    postal_code='postalCode0',
    state_or_province='stateOrProvince6'
)
```

