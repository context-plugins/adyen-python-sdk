
# Reconciliation Type

Possible values:

* **SaleReconciliation**
* **AcquirerSynchronisation**
* **AcquirerReconciliation**
* **PreviousReconciliation**

## Enumeration

`ReconciliationType`

## Fields

| Name |
|  --- |
| `SALERECONCILIATION` |
| `ACQUIRERSYNCHRONISATION` |
| `ACQUIRERRECONCILIATION` |
| `PREVIOUSRECONCILIATION` |

## Example

```python
from adyen.models.reconciliation_type import ReconciliationType

reconciliation_type = ReconciliationType.ACQUIRERRECONCILIATION
```

