
# Legal Entity Enum

The legal entity type of the account holder. This determines the information that should be provided in the request.

Possible values: **Business**, **Individual**, or **NonProfit**.

* If set to **Business** or **NonProfit**, then `accountHolderDetails.businessDetails` must be provided, with at least one entry in the `accountHolderDetails.businessDetails.shareholders` list.

* If set to **Individual**, then `accountHolderDetails.individualDetails` must be provided.

## Enumeration

`LegalEntityEnum`

## Fields

| Name |
|  --- |
| `BUSINESS` |
| `INDIVIDUAL` |
| `NONPROFIT` |
| `PARTNERSHIP` |
| `PUBLICCOMPANY` |

## Example

```python
from adyen.models.legal_entity_enum import LegalEntityEnum

legal_entity = LegalEntityEnum.PARTNERSHIP
```

