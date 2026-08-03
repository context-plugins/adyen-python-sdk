
# Sale Data 1

Data related to the Sale System.

*This model accepts additional fields of type Any.*

## Structure

`SaleData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operator_id` | `str` | Optional | Identification of the Cashier or Operator.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `operator_language` | `str` | Optional | Language of the Cashier or Operator.<br>If different from the Login.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `shift_number` | `str` | Optional | Shift number.<br>If different from the Login, see Login SaleData.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `sale_transaction_id` | [`SaleTransactionId`](../../doc/models/sale-transaction-id.md) | Required | - |
| `sale_reference_id` | `str` | Optional | Identification of a Sale global transaction for a sequence of related POI transactions.<br>If payment reservation.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `sale_terminal_data` | [`SaleTerminalData3`](../../doc/models/sale-terminal-data-3.md) | Optional | - |
| `token_requested_type` | [`TokenRequestedType1`](../../doc/models/token-requested-type-1.md) | Optional | - |
| `customer_order_id` | `str` | Optional | Additional and optional identification of a customer order.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `customer_order_req` | [`List[CustomerOrderReq]`](../../doc/models/customer-order-req.md) | Optional | List of customer order open, closed or both to be sent in the response messages.<br>Possible values:<br><br>* **Both**<br>* **Closed**<br>* **Open** |
| `sale_to_poi_data` | `str` | Optional | Sale information intended for the POI.<br>Stored with the transaction.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `sale_to_acquirer_data` | `str` | Optional | Sale information intended for the Acquirer.<br>Send to the Acquirer if present.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `sale_to_issuer_data` | [`SaleToIssuerData2`](../../doc/models/sale-to-issuer-data-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.sale_data_1 import SaleData1
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.sale_transaction_id import SaleTransactionId

sale_data_1 = SaleData1(
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
)
```

