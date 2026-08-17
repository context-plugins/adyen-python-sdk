
# Vat Absence Reason Enum

The reason the organization has not provided a VAT number.

Possible values: **industryExemption**, **belowTaxThreshold**.

## Enumeration

`VatAbsenceReasonEnum`

## Fields

| Name |
|  --- |
| `INDUSTRYEXEMPTION` |
| `BELOWTAXTHRESHOLD` |

## Example

```python
from adyen.models.vat_absence_reason_enum import VatAbsenceReasonEnum

vat_absence_reason = VatAbsenceReasonEnum.INDUSTRYEXEMPTION
```

