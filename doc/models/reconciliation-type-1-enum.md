
# Reconciliation Type 1 Enum

Type of Reconciliation requested by the Sale to the POI.
Possible values:

* **AcquirerReconciliation**
* **AcquirerSynchronisation**
* **PreviousReconciliation**
* **SaleReconciliation**

## Enumeration

`ReconciliationType1Enum`

## Fields

| Name |
|  --- |
| `SALERECONCILIATION` |
| `ACQUIRERSYNCHRONISATION` |
| `ACQUIRERRECONCILIATION` |
| `PREVIOUSRECONCILIATION` |

## Example

```python
from adyen.models.reconciliation_type_1_enum import ReconciliationType1Enum

reconciliation_type_1 = ReconciliationType1Enum.ACQUIRERRECONCILIATION
```

