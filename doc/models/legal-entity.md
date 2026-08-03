
# Legal Entity

The legal entity type of the account holder. This determines the information that should be provided in the request.

Possible values: **Business**, **Individual**, or **NonProfit**.

* If set to **Business** or **NonProfit**, then `accountHolderDetails.businessDetails` must be provided, with at least one entry in the `accountHolderDetails.businessDetails.shareholders` list.

* If set to **Individual**, then `accountHolderDetails.individualDetails` must be provided.

## Enumeration

`LegalEntity`

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
from adyen.models.legal_entity import LegalEntity

legal_entity = LegalEntity.PARTNERSHIP
```

