
# Phone Type Enum

The type of the phone number.

> The following values are permitted: `Landline`, `Mobile`, `SIP`, `Fax`., The type of the phone number.
> Possible values: **Landline**, **Mobile**, **SIP**, **Fax**.

## Enumeration

`PhoneTypeEnum`

## Fields

| Name |
|  --- |
| `FAX` |
| `LANDLINE` |
| `MOBILE` |
| `SIP` |

## Example

```python
from adyen.models.phone_type_enum import PhoneTypeEnum

phone_type = PhoneTypeEnum.MOBILE
```

