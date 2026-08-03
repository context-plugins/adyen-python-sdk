
# Business Type

The organization's business type.

Possible values: **other**, **listedPublicCompany**, **subsidiaryOfListedPublicCompany**, **governmentalOrganization**, **internationalOrganization**, **financialInstitution**.

## Enumeration

`BusinessType`

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
from adyen.models.business_type import BusinessType

business_type = BusinessType.SUBSIDIARYOFLISTEDPUBLICCOMPANY
```

