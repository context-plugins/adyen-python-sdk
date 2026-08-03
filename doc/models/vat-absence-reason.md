
# Vat Absence Reason

The reason the organization has not provided a VAT number.

Possible values: **industryExemption**, **belowTaxThreshold**.

## Enumeration

`VatAbsenceReason`

## Fields

| Name |
|  --- |
| `INDUSTRYEXEMPTION` |
| `BELOWTAXTHRESHOLD` |

## Example

```python
from adyen.models.vat_absence_reason import VatAbsenceReason

vat_absence_reason = VatAbsenceReason.INDUSTRYEXEMPTION
```

