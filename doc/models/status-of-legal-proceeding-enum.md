
# Status of Legal Proceeding Enum

The status of any current or past legal action taken against the legal entity.

Possible values: **noLegalActionsTaken**, **underJudicialAdministration**, **bankruptcyInsolvency**, **otherLegalMeasures**

If the value of this field is **noLegalActionsTaken**, then `dateOfInitiationOfLegalProceeding` is not required. Otherwise, it is required.

## Enumeration

`StatusOfLegalProceedingEnum`

## Fields

| Name |
|  --- |
| `NOLEGALACTIONSTAKEN` |
| `UNDERJUDICIALADMINISTRATION` |
| `BANKRUPTCYINSOLVENCY` |
| `OTHERLEGALMEASURES` |

## Example

```python
from adyen.models.status_of_legal_proceeding_enum import StatusOfLegalProceedingEnum

status_of_legal_proceeding = StatusOfLegalProceedingEnum.BANKRUPTCYINSOLVENCY
```

