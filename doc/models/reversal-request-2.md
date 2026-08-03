
# Reversal Request 2

Content of the Reversal Request message.

*This model accepts additional fields of type Any.*

## Structure

`ReversalRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_data` | [`SaleData2`](../../doc/models/sale-data-2.md) | Optional | - |
| `original_poi_transaction` | [`OriginalPoiTransaction3`](../../doc/models/original-poi-transaction-3.md) | Required | - |
| `reversed_amount` | `float` | Optional | Amount of the payment or loyalty to reverse.<br>ReversedAmount is implicitly equal to the AuthorizedAmount if absent.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `reversal_reason` | [`ReversalReason1`](../../doc/models/reversal-reason-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.original_poi_transaction_3 import OriginalPoiTransaction3
from adyen.models.poi_transaction_id import PoiTransactionId
from adyen.models.reversal_reason_1 import ReversalReason1
from adyen.models.reversal_request_2 import ReversalRequest2
from adyen.models.sale_data_2 import SaleData2
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.sale_transaction_id import SaleTransactionId

reversal_request_2 = ReversalRequest2(
    original_poi_transaction=OriginalPoiTransaction3(
        sale_id='SaleID6',
        poiid='POIID0',
        poi_transaction_id=PoiTransactionId(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        reuse_card_data_flag=True,
        approval_code='ApprovalCode0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reversal_reason=ReversalReason1.MALFUNCTION,
    sale_data=SaleData2(
        sale_transaction_id=SaleTransactionId(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        operator_id='OperatorID8',
        operator_language='OperatorLanguage2',
        shift_number='ShiftNumber0',
        sale_reference_id='SaleReferenceID8',
        sale_terminal_data=SaleTerminalData3(
            totals_group_id='TotalsGroupID4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reversed_amount=23.38,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

