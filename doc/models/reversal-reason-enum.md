
# Reversal Reason Enum

Reason of the payment or loyalty reversal.
Possible values:

* **CustCancel**
* **MerchantCancel**
* **Malfunction**
* **Unable2Compl**

## Enumeration

`ReversalReasonEnum`

## Fields

| Name |
|  --- |
| `CUSTCANCEL` |
| `MERCHANTCANCEL` |
| `MALFUNCTION` |
| `UNABLE2COMPL` |

## Example

```python
from adyen.models.reversal_reason_enum import ReversalReasonEnum

reversal_reason = ReversalReasonEnum.MALFUNCTION
```

