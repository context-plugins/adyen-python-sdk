
# Payment Acquirer Data 1

*This model accepts additional fields of type Any.*

## Structure

`PaymentAcquirerData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquirer_id` | `int` | Optional | Identification of the Acquirer.<br>Identification of the Acquirer when the POI System is multi-acquirer. |
| `merchant_id` | `str` | Required | Identification of the Merchant for the Acquirer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `acquirer_poiid` | `str` | Required | Identification of the POI for the payment Acquirer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `acquirer_transaction_id` | [`AcquirerTransactionId`](../../doc/models/acquirer-transaction-id.md) | Optional | - |
| `approval_code` | `str` | Optional | Code assigned to a transaction approval by the Acquirer.<br>If available.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `host_reconciliation_id` | `str` | Optional | Identifier of a reconciliation period with a payment or loyalty host. Allows the assignment of a transaction to the Acquirer reconciliation (or batch).<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.acquirer_transaction_id import AcquirerTransactionId
from adyen.models.payment_acquirer_data_1 import PaymentAcquirerData1

payment_acquirer_data_1 = PaymentAcquirerData1(
    merchant_id='MerchantID8',
    acquirer_poiid='AcquirerPOIID8',
    acquirer_id=210,
    acquirer_transaction_id=AcquirerTransactionId(
        transaction_id='TransactionID2',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    approval_code='ApprovalCode2',
    host_reconciliation_id='HostReconciliationID2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

