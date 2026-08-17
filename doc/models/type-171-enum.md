
# Type 171 Enum

Type of trust.

See possible values for trusts in [Australia](https://docs.adyen.com/platforms/verification-requirements/?tab=trust_3_4#trust-types-in-australia) and [New Zealand](https://docs.adyen.com/platforms/verification-requirements/?tab=trust_3_4#trust-types-in-new-zealand).

## Enumeration

`Type171Enum`

## Fields

| Name |
|  --- |
| `BUSINESSTRUST` |
| `CASHMANAGEMENTTRUST` |
| `CHARITABLETRUST` |
| `CORPORATEUNITTRUST` |
| `DECEASEDESTATE` |
| `DISCRETIONARYTRUST` |
| `DISCRETIONARYINVESTMENTTRUST` |
| `DISCRETIONARYSERVICESMANAGEMENTTRUST` |
| `DISCRETIONARYTRADINGTRUST` |
| `FAMILYTRUST` |
| `FIRSTHOMESAVERACCOUNTSTRUST` |
| `FIXEDTRUST` |
| `FIXEDUNITTRUST` |
| `HYBRIDTRUST` |
| `LISTEDPUBLICUNITTRUST` |
| `OTHERTRUST` |
| `POOLEDSUPERANNUATIONTRUST` |
| `PUBLICTRADINGTRUST` |
| `UNLISTEDPUBLICUNITTRUST` |

## Example

```python
from adyen.models.type_171_enum import Type171Enum

type_171 = Type171Enum.CASHMANAGEMENTTRUST
```

