
# Legal Form Enum

The form of legal arrangement. Required if `type` is **Trust** or **Partnership**.

The possible values depend on the `type`.

- For `type` **Trust**:  **CashManagementTrust**, **CorporateUnitTrust**, **DeceasedEstate**, **DiscretionaryInvestmentTrust**, **DiscretionaryServicesManagementTrust**, **DiscretionaryTradingTrust**, **FirstHomeSaverAccountsTrust**, **FixedTrust**, **FixedUnitTrust**, **HybridTrust**, **ListedPublicUnitTrust**, **OtherTrust**, **PooledSuperannuationTrust**, **PublicTradingTrust**, or **UnlistedPublicUnitTrust**.

- For `type` **Partnership**: **LimitedPartnership**, **FamilyPartnership**, or **OtherPartnership**

## Enumeration

`LegalFormEnum`

## Fields

| Name |
|  --- |
| `CASHMANAGEMENTTRUST` |
| `CORPORATEUNITTRUST` |
| `DECEASEDESTATE` |
| `DISCRETIONARYINVESTMENTTRUST` |
| `DISCRETIONARYSERVICESMANAGEMENTTRUST` |
| `DISCRETIONARYTRADINGTRUST` |
| `FIRSTHOMESAVERACCOUNTSTRUST` |
| `FIXEDTRUST` |
| `FIXEDUNITTRUST` |
| `HYBRIDTRUST` |
| `LISTEDPUBLICUNITTRUST` |
| `OTHERTRUST` |
| `POOLEDSUPERANNUATIONTRUST` |
| `PUBLICTRADINGTRUST` |
| `UNLISTEDPUBLICUNITTRUST` |
| `LIMITEDPARTNERSHIP` |
| `FAMILYPARTNERSHIP` |
| `OTHERPARTNERSHIP` |

## Example

```python
from adyen.models.legal_form_enum import LegalFormEnum

legal_form = LegalFormEnum.FAMILYPARTNERSHIP
```

