
# Loyalty Acquirer Data

## Structure

`LoyaltyAcquirerData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_acquirer_id` | `str` | Optional | Identification of the loyalty Acquirer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `approval_code` | `str` | Optional | Code assigned to a transaction approval by the Acquirer. Could be an identifier of the approved transaction for the Acquirer. This data element is conditional for the Loyalty Acquirers. Used in the PaymentRequest request for a referral.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `loyalty_transaction_id` | [`TransactionIDType`](../../doc/models/transaction-id-type.md) | Optional | Identification of a transaction for the Sale System or the POI System. |
| `host_reconciliation_id` | `str` | Optional | Identifier of a reconciliation period with a payment or loyalty host. Allows the assignment of a transaction to the Acquirer reconciliation (or batch).<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
import dateutil.parser

from adyen.models.loyalty_acquirer_data import LoyaltyAcquirerData
from adyen.models.transaction_id_type import TransactionIDType

loyalty_acquirer_data = LoyaltyAcquirerData(
    loyalty_acquirer_id='LoyaltyAcquirerID6',
    approval_code='ApprovalCode4',
    loyalty_transaction_id=TransactionIDType(
        transaction_id='TransactionID6',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ),
    host_reconciliation_id='HostReconciliationID4'
)
```

