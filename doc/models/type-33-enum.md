
# Type 33 Enum

Type of entity.

Possible values: **LegalEntity**, **BankAccount**, **Document**.

## Enumeration

`Type33Enum`

## Fields

| Name |
|  --- |
| `BANKACCOUNT` |
| `DOCUMENT` |
| `LEGALENTITY` |

## Example

```python
from adyen.models.type_33_enum import Type33Enum

type_33 = Type33Enum.BANKACCOUNT
```

