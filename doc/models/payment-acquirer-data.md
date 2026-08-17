
# Payment Acquirer Data

Data related to the response from the payment Acquirer.

## Structure

`PaymentAcquirerData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquirer_id` | `int` | Optional | Identification of the Acquirer.<br>Identification of the Acquirer when the POI System is multi-acquirer. |
| `merchant_id` | `str` | Required | Identification of the Merchant for the Acquirer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `acquirer_poiid` | `str` | Required | Identification of the POI for the payment Acquirer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `acquirer_transaction_id` | [`TransactionIDType6`](../../doc/models/transaction-id-type-6.md) | Optional | Identification of the Transaction for the Acquirer.<br>If provided by the Acquirer. |
| `approval_code` | `str` | Optional | Code assigned to a transaction approval by the Acquirer.<br>If available.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `host_reconciliation_id` | `str` | Optional | Identifier of a reconciliation period with a payment or loyalty host. Allows the assignment of a transaction to the Acquirer reconciliation (or batch).<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
import dateutil.parser

from adyen.models.payment_acquirer_data import PaymentAcquirerData
from adyen.models.transaction_id_type_6 import TransactionIDType6

payment_acquirer_data = PaymentAcquirerData(
    merchant_id='MerchantID4',
    acquirer_poiid='AcquirerPOIID4',
    acquirer_id=74,
    acquirer_transaction_id=TransactionIDType6(
        transaction_id='TransactionID2',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ),
    approval_code='ApprovalCode8',
    host_reconciliation_id='HostReconciliationID8'
)
```

