
# Identification Type Enum

The type of the identification.

Possible values: **iban**, **routingNumber**, **sortCode**, **bic**.

## Enumeration

`IdentificationTypeEnum`

## Fields

| Name |
|  --- |
| `BIC` |
| `IBAN` |
| `ROUTINGNUMBER` |
| `SORTCODE` |

## Example

```python
from adyen.models.identification_type_enum import IdentificationTypeEnum

identification_type = IdentificationTypeEnum.BIC
```

