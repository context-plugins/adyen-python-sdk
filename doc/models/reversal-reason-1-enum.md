
# Reversal Reason 1 Enum

Reason of the payment or loyalty reversal.
Possible values:

* **CustCancel**
* **Malfunction**
* **MerchantCancel**
* **Unable2Compl**

## Enumeration

`ReversalReason1Enum`

## Fields

| Name |
|  --- |
| `CUSTCANCEL` |
| `MERCHANTCANCEL` |
| `MALFUNCTION` |
| `UNABLE2COMPL` |

## Example

```python
from adyen.models.reversal_reason_1_enum import ReversalReason1Enum

reversal_reason_1 = ReversalReason1Enum.CUSTCANCEL
```

