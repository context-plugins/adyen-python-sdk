
# Print Response

It conveys the result of the print, parallel to the message request, except if response not required and absent.
Content of the Print Response message.

## Structure

`PrintResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_qualifier` | [`DocumentQualifier2Enum`](../../doc/models/document-qualifier-2-enum.md) | Required | Qualification of the document to print to the Cashier or the Customer. Allows the manager of the printer, Sale or POI Terminal, to send information to a physical printer or to use the paper type accordingly.<br>Possible values:<br><br>* **CashierReceipt**<br>* **CustomerReceipt**<br>* **Document**<br>* **Journal**<br>* **SaleReceipt**<br>* **Voucher** |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |

## Example

```python
from adyen.models.document_qualifier_2_enum import DocumentQualifier2Enum
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.print_response import PrintResponse
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

print_response = PrintResponse(
    document_qualifier=DocumentQualifier2Enum.VOUCHER,
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    )
)
```

