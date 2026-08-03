
# Status of Legal Proceeding

The status of any current or past legal action taken against the legal entity.

Possible values: **noLegalActionsTaken**, **underJudicialAdministration**, **bankruptcyInsolvency**, **otherLegalMeasures**

If the value of this field is **noLegalActionsTaken**, then `dateOfInitiationOfLegalProceeding` is not required. Otherwise, it is required.

## Enumeration

`StatusOfLegalProceeding`

## Fields

| Name |
|  --- |
| `NOLEGALACTIONSTAKEN` |
| `UNDERJUDICIALADMINISTRATION` |
| `BANKRUPTCYINSOLVENCY` |
| `OTHERLEGALMEASURES` |

## Example

```python
from adyen.models.status_of_legal_proceeding import StatusOfLegalProceeding

status_of_legal_proceeding = StatusOfLegalProceeding.BANKRUPTCYINSOLVENCY
```

