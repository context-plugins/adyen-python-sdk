
# Type 110 Enum

The [type of legal arrangement](https://docs.adyen.com/classic-platforms/verification-process/legal-arrangements#types-of-legal-arrangements).

Possible values:

- **Association**

- **Partnership**

- **SoleProprietorship**

- **Trust**

## Enumeration

`Type110Enum`

## Fields

| Name |
|  --- |
| `ASSOCIATION` |
| `PARTNERSHIP` |
| `SOLEPROPRIETORSHIP` |
| `TRUST` |

## Example

```python
from adyen.models.type_110_enum import Type110Enum

type_110 = Type110Enum.SOLEPROPRIETORSHIP
```

