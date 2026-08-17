
# Document Qualifier Enum

Possible values:

* **SaleReceipt**
* **CashierReceipt**
* **CustomerReceipt**
* **Document**
* **Voucher**
* **Journal**

## Enumeration

`DocumentQualifierEnum`

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
from adyen.models.document_qualifier_enum import DocumentQualifierEnum

document_qualifier = DocumentQualifierEnum.VOUCHER
```

