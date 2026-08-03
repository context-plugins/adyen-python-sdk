
# Reversal Reason

Reason of the payment or loyalty reversal.
Possible values:

* **CustCancel**
* **MerchantCancel**
* **Malfunction**
* **Unable2Compl**

## Enumeration

`ReversalReason`

## Fields

| Name |
|  --- |
| `CUSTCANCEL` |
| `MERCHANTCANCEL` |
| `MALFUNCTION` |
| `UNABLE2COMPL` |

## Example

```python
from adyen.models.reversal_reason import ReversalReason

reversal_reason = ReversalReason.MALFUNCTION
```

