
# Phone Number

## Structure

`PhoneNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `str` | Required | The full phone number, including the country code. For example, **+3112345678**. |
| `phone_country_code` | `str` | Optional, Read-only | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code prefix of the phone number. For example, **US** or **NL**.<br><br>The value of the `phoneCountryCode` is determined by the country code digit(s) of `phone.number` |
| `mtype` | `str` | Optional | The type of phone number.<br>Possible values: **mobile**, **landline**, **sip**, **fax.** |

## Example

```python
from adyen.models.phone_number import PhoneNumber

phone_number = PhoneNumber(
    number='number0',
    mtype='type8'
)
```

