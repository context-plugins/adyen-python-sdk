
# Document Qualifier

Possible values:

* **SaleReceipt**
* **CashierReceipt**
* **CustomerReceipt**
* **Document**
* **Voucher**
* **Journal**

## Enumeration

`DocumentQualifier`

## Fields

| Name |
|  --- |
| `SALERECEIPT` |
| `CASHIERRECEIPT` |
| `CUSTOMERRECEIPT` |
| `DOCUMENT` |
| `VOUCHER` |
| `JOURNAL` |

## Example

```python
from adyen.models.document_qualifier import DocumentQualifier

document_qualifier = DocumentQualifier.VOUCHER
```

