
# Reversal Request

It conveys Information related to the reversal of a previous payment or a loyalty transaction.
Content of the Reversal Request message.

## Structure

`ReversalRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_data` | [`SaleData`](../../doc/models/sale-data.md) | Optional | Data associated with the Sale System, with a particular value during the processing of the payment by the POI, including the cards acquisition. |
| `original_poi_transaction` | [`OriginalPOITransaction2`](../../doc/models/original-poi-transaction-2.md) | Required | Identification of a previous POI transaction. |
| `reversed_amount` | `float` | Optional | Amount of the payment or loyalty to reverse.<br>ReversedAmount is implicitly equal to the AuthorizedAmount if absent.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `reversal_reason` | [`ReversalReason1Enum`](../../doc/models/reversal-reason-1-enum.md) | Required | Reason of the payment or loyalty reversal.<br>Possible values:<br><br>* **CustCancel**<br>* **Malfunction**<br>* **MerchantCancel**<br>* **Unable2Compl** |

## Example

```python
import dateutil.parser

from adyen.models.original_poi_transaction_2 import OriginalPOITransaction2
from adyen.models.reversal_reason_1_enum import ReversalReason1Enum
from adyen.models.reversal_request import ReversalRequest
from adyen.models.sale_data import SaleData
from adyen.models.sale_terminal_data_1 import SaleTerminalData1
from adyen.models.transaction_id_type_1 import TransactionIDType1
from adyen.models.transaction_id_type_4 import TransactionIDType4

reversal_request = ReversalRequest(
    original_poi_transaction=OriginalPOITransaction2(
        sale_id='SaleID6',
        poiid='POIID0',
        poi_transaction_id=TransactionIDType4(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        reuse_card_data_flag=True,
        approval_code='ApprovalCode0'
    ),
    reversal_reason=ReversalReason1Enum.MALFUNCTION,
    sale_data=SaleData(
        sale_transaction_id=TransactionIDType1(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        operator_id='OperatorID8',
        operator_language='OperatorLanguage2',
        shift_number='ShiftNumber0',
        sale_reference_id='SaleReferenceID8',
        sale_terminal_data=SaleTerminalData1(
            totals_group_id='TotalsGroupID4'
        )
    ),
    reversed_amount=47.1
)
```

