
# Transaction Status Request

Content of the TransactionStatus Request message.
It conveys Information requested for status of the last or current Payment, Loyalty or Reversal transaction.

*This model accepts additional fields of type Any.*

## Structure

`TransactionStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_reference` | [`MessageReference1`](../../doc/models/message-reference-1.md) | Optional | - |
| `receipt_reprint_flag` | `bool` | Optional | Request to reprint the POI receipt(s). Allows reprinting a receipt with a `TransactionStatus` message<br><br>**Default**: `False` |
| `document_qualifier` | [`List[DocumentQualifier]`](../../doc/models/document-qualifier.md) | Optional | Qualification of the document to print to the Cashier or the Customer. Allows the manager of the printer, Sale or POI Terminal, to send the information to a particular physical printer or to use the paper type accordingly.<br>Possible values:<br><br>* **CashierReceipt**<br>* **CustomerReceipt**<br>* **Document**<br>* **Journal**<br>* **SaleReceipt**<br>* **Voucher** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.document_qualifier import DocumentQualifier
from adyen.models.message_category_2 import MessageCategory2
from adyen.models.message_reference_1 import MessageReference1
from adyen.models.transaction_status_request import TransactionStatusRequest

transaction_status_request = TransactionStatusRequest(
    message_reference=MessageReference1(
        message_category=MessageCategory2.PAYMENT,
        service_id='ServiceID0',
        device_id='DeviceID2',
        sale_id='SaleID8',
        poiid='POIID2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    receipt_reprint_flag=False,
    document_qualifier=[
        DocumentQualifier.CASHIERRECEIPT,
        DocumentQualifier.CUSTOMERRECEIPT,
        DocumentQualifier.DOCUMENT
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

