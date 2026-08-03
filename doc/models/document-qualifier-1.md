
# Document Qualifier 1

Qualification of the document to print to the Cashier or the Customer.
SaleReceipt or CashierReceipt.
Possible values:

* **CashierReceipt**
* **CustomerReceipt**
* **Document**
* **Journal**
* **SaleReceipt**
* **Voucher**

## Enumeration

`DocumentQualifier1`

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
from adyen.models.document_qualifier_1 import DocumentQualifier1

document_qualifier_1 = DocumentQualifier1.CUSTOMERRECEIPT
```

