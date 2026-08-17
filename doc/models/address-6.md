
# Address 6

## Structure

`Address6`

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
from adyen.models.address_6 import Address6

address_6 = Address6(
    country='country8',
    city='city6',
    line_1='line16',
    line_2='line28',
    postal_code='postalCode4',
    state_or_province='stateOrProvince2'
)
```

