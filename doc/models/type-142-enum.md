
# Type 142 Enum

Defines the relationship of the legal entity to the current legal entity.

Possible value for individuals: **legalRepresentative**.

Possible values for organizations: **director**, **signatory**, **trustOwnership**, **uboThroughOwnership**, **uboThroughControl**, **ultimateParentCompany**, or **immediateParentCompany**.

Possible values for sole proprietorships: **soleProprietorship**.

Possible value for trusts: **trust**.

Possible values for trust members: **definedBeneficiary**, **protector**, **secondaryTrustee**, **settlor**, **uboThroughControl**, or **uboThroughOwnership**.

Possible value for unincorporated partnership: **unincorporatedPartnership**.

Possible values for unincorporated partnership members: **secondaryPartner**, **uboThroughControl**, **uboThroughOwnership**

## Enumeration

`Type142Enum`

## Fields

| Name |
|  --- |
| `DEFINEDBENEFICIARY` |
| `DIRECTOR` |
| `IMMEDIATEPARENTCOMPANY` |
| `LEGALREPRESENTATIVE` |
| `PCISIGNATORY` |
| `PROTECTOR` |
| `SECONDARYPARTNER` |
| `SECONDARYTRUSTEE` |
| `SETTLOR` |
| `SIGNATORY` |
| `SOLEPROPRIETORSHIP` |
| `TRUST` |
| `TRUSTOWNERSHIP` |
| `UBOTHROUGHCONTROL` |
| `UBOTHROUGHOWNERSHIP` |
| `ULTIMATEPARENTCOMPANY` |
| `UNDEFINEDBENEFICIARY` |
| `UNINCORPORATEDPARTNERSHIP` |

## Example

```python
from adyen.models.type_142_enum import Type142Enum

type_142 = Type142Enum.UBOTHROUGHOWNERSHIP
```

