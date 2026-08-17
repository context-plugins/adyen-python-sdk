
# Type 151 Enum

The tax reporting classification type.

Possible values: **nonFinancialNonReportable**, **financialNonReportable**, **nonFinancialActive**, **nonFinancialPassive**.

## Enumeration

`Type151Enum`

## Fields

| Name |
|  --- |
| `NONFINANCIALNONREPORTABLE` |
| `FINANCIALNONREPORTABLE` |
| `NONFINANCIALACTIVE` |
| `NONFINANCIALPASSIVE` |

## Example

```python
from adyen.models.type_151_enum import Type151Enum

type_151 = Type151Enum.NONFINANCIALACTIVE
```

