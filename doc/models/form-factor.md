
# Form Factor

Business accounts with a `formFactor` value of **physical** are business accounts issued under the central bank of that country. The default value is **physical** for NL, US, and UK business accounts.

Adyen creates a local IBAN for business accounts when the `formFactor` value is set to **virtual**. The local IBANs that are supported are for DE and FR, which reference a physical NL account, with funds being routed through the central bank of NL.

## Enumeration

`FormFactor`

## Fields

| Name |
|  --- |
| `PHYSICAL` |
| `UNKNOWN` |
| `VIRTUAL` |

## Example

```python
from adyen.models.form_factor import FormFactor

form_factor = FormFactor.VIRTUAL
```

