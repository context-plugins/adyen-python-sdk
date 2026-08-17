
# Document Qualifier 1 Enum

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

`DocumentQualifier1Enum`

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
from adyen.models.document_qualifier_1_enum import DocumentQualifier1Enum

document_qualifier_1 = DocumentQualifier1Enum.CUSTOMERRECEIPT
```

