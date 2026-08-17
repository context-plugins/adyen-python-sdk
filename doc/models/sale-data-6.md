
# Sale Data 6

Data related to the Sale System.
Copy.

## Structure

`SaleData6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operator_id` | `str` | Optional | Identification of the Cashier or Operator.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `operator_language` | `str` | Optional | Language of the Cashier or Operator.<br>If different from the Login.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `shift_number` | `str` | Optional | Shift number.<br>If different from the Login, see Login SaleData.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `sale_transaction_id` | [`TransactionIDType1`](../../doc/models/transaction-id-type-1.md) | Required | Identification of a Sale transaction. |
| `sale_reference_id` | `str` | Optional | Identification of a Sale global transaction for a sequence of related POI transactions.<br>If payment reservation.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `sale_terminal_data` | [`SaleTerminalData1`](../../doc/models/sale-terminal-data-1.md) | Optional | Information related to the software and hardware features of the Sale Terminal.<br>If content is not empty. |
| `token_requested_type` | [`TokenRequestedType1Enum`](../../doc/models/token-requested-type-1-enum.md) | Optional | Type of token replacing the PAN of a payment card to identify the payment<br>mean of the customer. It allows, for a merchant, to use a token for a transaction<br>only or for a longer period.<br>Possible values:<br><br>* **Customer**<br>* **Transaction** |
| `customer_order_id` | `str` | Optional | Additional and optional identification of a customer order.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `customer_order_req` | [`List[CustomerOrderReqEnum]`](../../doc/models/customer-order-req-enum.md) | Optional | List of customer order open, closed or both to be sent in the response messages.<br>Possible values:<br><br>* **Both**<br>* **Closed**<br>* **Open** |
| `sale_to_poi_data` | `str` | Optional | Sale information intended for the POI.<br>Stored with the transaction.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `sale_to_acquirer_data` | `str` | Optional | Sale information intended for the Acquirer.<br>Send to the Acquirer if present.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `sale_to_issuer_data` | [`SaleToIssuerData1`](../../doc/models/sale-to-issuer-data-1.md) | Optional | Sale information intended for the Issuer.<br>Send to the Acquirer if present. |

## Example

```python
import dateutil.parser

from adyen.models.sale_data_6 import SaleData6
from adyen.models.sale_terminal_data_1 import SaleTerminalData1
from adyen.models.transaction_id_type_1 import TransactionIDType1

sale_data_6 = SaleData6(
    sale_transaction_id=TransactionIDType1(
        transaction_id='TransactionID2',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ),
    operator_id='OperatorID6',
    operator_language='OperatorLanguage0',
    shift_number='ShiftNumber8',
    sale_reference_id='SaleReferenceID0',
    sale_terminal_data=SaleTerminalData1(
        totals_group_id='TotalsGroupID4'
    )
)
```

