
# Transaction Status Request 2

Content of the TransactionStatus Request message.

## Structure

`TransactionStatusRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_reference` | [`MessageReference2`](../../doc/models/message-reference-2.md) | Optional | Identification of a previous POI transaction.<br>Present if it contains any data. |
| `receipt_reprint_flag` | `bool` | Optional | Request to reprint the POI receipt(s). Allows reprinting a receipt with a `TransactionStatus` message<br><br>**Default**: `False` |
| `document_qualifier` | [`List[DocumentQualifierEnum]`](../../doc/models/document-qualifier-enum.md) | Optional | Qualification of the document to print to the Cashier or the Customer. Allows the manager of the printer, Sale or POI Terminal, to send the information to a particular physical printer or to use the paper type accordingly.<br>Possible values:<br><br>* **CashierReceipt**<br>* **CustomerReceipt**<br>* **Document**<br>* **Journal**<br>* **SaleReceipt**<br>* **Voucher** |

## Example

```python
from adyen.models.document_qualifier_enum import DocumentQualifierEnum
from adyen.models.message_category_2_enum import MessageCategory2Enum
from adyen.models.message_reference_2 import MessageReference2
from adyen.models.transaction_status_request_2 import TransactionStatusRequest2

transaction_status_request_2 = TransactionStatusRequest2(
    message_reference=MessageReference2(
        message_category=MessageCategory2Enum.PAYMENT,
        service_id='ServiceID0',
        device_id='DeviceID2',
        sale_id='SaleID8',
        poiid='POIID2'
    ),
    receipt_reprint_flag=False,
    document_qualifier=[
        DocumentQualifierEnum.CASHIERRECEIPT,
        DocumentQualifierEnum.CUSTOMERRECEIPT,
        DocumentQualifierEnum.DOCUMENT
    ]
)
```

