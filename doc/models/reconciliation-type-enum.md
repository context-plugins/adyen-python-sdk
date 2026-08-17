
# Reconciliation Type Enum

Possible values:

* **SaleReconciliation**
* **AcquirerSynchronisation**
* **AcquirerReconciliation**
* **PreviousReconciliation**

## Enumeration

`ReconciliationTypeEnum`

## Fields

| Name |
|  --- |
| `SALERECONCILIATION` |
| `ACQUIRERSYNCHRONISATION` |
| `ACQUIRERRECONCILIATION` |
| `PREVIOUSRECONCILIATION` |

## Example

```python
from adyen.models.reconciliation_type_enum import ReconciliationTypeEnum

reconciliation_type = ReconciliationTypeEnum.ACQUIRERRECONCILIATION
```

