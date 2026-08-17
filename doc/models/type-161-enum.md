
# Type 161 Enum

Type of organization.

Possible values: **associationIncorporated**, **governmentalOrganization**, **listedPublicCompany**, **nonProfit**, **partnershipIncorporated**, **privateCompany**.

## Enumeration

`Type161Enum`

## Fields

| Name |
|  --- |
| `ASSOCIATIONINCORPORATED` |
| `GOVERNMENTALORGANIZATION` |
| `LISTEDPUBLICCOMPANY` |
| `NONPROFIT` |
| `PARTNERSHIPINCORPORATED` |
| `PRIVATECOMPANY` |

## Example

```python
from adyen.models.type_161_enum import Type161Enum

type_161 = Type161Enum.LISTEDPUBLICCOMPANY
```

