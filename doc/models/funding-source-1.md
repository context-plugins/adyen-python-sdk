
# Funding Source 1

The funding source of the payment method.

Possible values:

* **credit**
* **debit**
* **prepaid**
* **deferred_debit**
* **charged**
* **ANY**

## Enumeration

`FundingSource1`

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
from adyen.models.funding_source_1 import FundingSource1

funding_source_1 = FundingSource1.PREPAID
```

