
# Reconciliation Type 1

Type of Reconciliation requested by the Sale to the POI.
Possible values:

* **AcquirerReconciliation**
* **AcquirerSynchronisation**
* **PreviousReconciliation**
* **SaleReconciliation**

## Enumeration

`ReconciliationType1`

## Fields

| Name |
|  --- |
| `SALERECONCILIATION` |
| `ACQUIRERSYNCHRONISATION` |
| `ACQUIRERRECONCILIATION` |
| `PREVIOUSRECONCILIATION` |

## Example

```python
from adyen.models.reconciliation_type_1 import ReconciliationType1

reconciliation_type_1 = ReconciliationType1.ACQUIRERRECONCILIATION
```

