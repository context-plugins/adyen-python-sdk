
# Reversal Reason 1

Reason of the payment or loyalty reversal.
Possible values:

* **CustCancel**
* **Malfunction**
* **MerchantCancel**
* **Unable2Compl**

## Enumeration

`ReversalReason1`

## Fields

| Name |
|  --- |
| `CUSTCANCEL` |
| `MERCHANTCANCEL` |
| `MALFUNCTION` |
| `UNABLE2COMPL` |

## Example

```python
from adyen.models.reversal_reason_1 import ReversalReason1

reversal_reason_1 = ReversalReason1.CUSTCANCEL
```

