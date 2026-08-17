
# Funding Source 1 Enum

The funding source of the payment method.

Possible values:

* **credit**
* **debit**
* **prepaid**
* **deferred_debit**
* **charged**
* **ANY**

## Enumeration

`FundingSource1Enum`

## Fields

| Name |
|  --- |
| `CHARGED` |
| `CREDIT` |
| `DEBIT` |
| `DEFERRED_DEBIT` |
| `PREPAID` |
| `ANY` |

## Example

```python
from adyen.models.funding_source_1_enum import FundingSource1Enum

funding_source_1 = FundingSource1Enum.PREPAID
```

