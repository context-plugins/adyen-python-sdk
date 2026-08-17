
# Business Type Enum

The organization's business type.

Possible values: **other**, **listedPublicCompany**, **subsidiaryOfListedPublicCompany**, **governmentalOrganization**, **internationalOrganization**, **financialInstitution**.

## Enumeration

`BusinessTypeEnum`

## Fields

| Name |
|  --- |
| `OTHER` |
| `LISTEDPUBLICCOMPANY` |
| `SUBSIDIARYOFLISTEDPUBLICCOMPANY` |
| `GOVERNMENTALORGANIZATION` |
| `INTERNATIONALORGANIZATION` |
| `FINANCIALINSTITUTION` |

## Example

```python
from adyen.models.business_type_enum import BusinessTypeEnum

business_type = BusinessTypeEnum.SUBSIDIARYOFLISTEDPUBLICCOMPANY
```

