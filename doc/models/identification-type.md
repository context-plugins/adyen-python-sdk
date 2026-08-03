
# Identification Type

The type of the identification.

Possible values: **iban**, **routingNumber**, **sortCode**, **bic**.

## Enumeration

`IdentificationType`

## Fields

| Name |
|  --- |
| `BIC` |
| `IBAN` |
| `ROUTINGNUMBER` |
| `SORTCODE` |

## Example

```python
from adyen.models.identification_type import IdentificationType

identification_type = IdentificationType.BIC
```

