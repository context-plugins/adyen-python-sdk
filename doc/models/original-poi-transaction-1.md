
# Original POI Transaction 1

Identification of a previous POI transaction.
If StoredValueTransactionType is Reverse or Duplicate.

## Structure

`OriginalPOITransaction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_id` | `str` | Optional | Identification of a Sale System for the NEXO SaletoPOI protocol.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `poiid` | `str` | Optional | Identification of a payment terminal for the NEXO SaletoPOI protocol.<br>If original transaction is coming from another POI.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `poi_transaction_id` | [`TransactionIDType4`](../../doc/models/transaction-id-type-4.md) | Optional | Unique identification of a POI transaction for a POI.<br>Absent if SaleReferenceID is sufficient to identify the transaction. |
| `reuse_card_data_flag` | `bool` | Optional | Indicates if the card data has to be retrieved from a previous transaction.<br><br>**Default**: `True` |
| `approval_code` | `str` | Optional | Code assigned to a transaction approval by the Acquirer.<br>If referral.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `acquirer_id` | `int` | Optional | Identification of the Acquirer.<br>Restrict to the Acquirer if present. |
| `amount_value` | `float` | Optional | Value of an amount.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `host_transaction_id` | [`TransactionIDType5`](../../doc/models/transaction-id-type-5.md) | Optional | Identification of the transaction by the host in charge of the stored value transaction.<br>If POITransactionID not present. |

## Example

```python
import dateutil.parser

from adyen.models.original_poi_transaction_1 import OriginalPOITransaction1
from adyen.models.transaction_id_type_4 import TransactionIDType4

original_poi_transaction_1 = OriginalPOITransaction1(
    sale_id='SaleID8',
    poiid='POIID6',
    poi_transaction_id=TransactionIDType4(
        transaction_id='TransactionID2',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ),
    reuse_card_data_flag=True,
    approval_code='ApprovalCode4'
)
```

