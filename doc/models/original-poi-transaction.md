
# Original Poi Transaction

Identification of a previous POI transaction.
In the Payment Request message, it allows using the card of a previous CardAcquisition or Payment request.

*This model accepts additional fields of type Any.*

## Structure

`OriginalPoiTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_id` | `str` | Optional | Identification of a Sale System for the NEXO SaletoPOI protocol.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `poiid` | `str` | Optional | Identification of a payment terminal for the NEXO SaletoPOI protocol.<br>If original transaction is coming from another POI.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `poi_transaction_id` | [`PoiTransactionId`](../../doc/models/poi-transaction-id.md) | Optional | - |
| `reuse_card_data_flag` | `bool` | Optional | Indicates if the card data has to be retrieved from a previous transaction.<br><br>**Default**: `True` |
| `approval_code` | `str` | Optional | Code assigned to a transaction approval by the Acquirer.<br>If referral.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `acquirer_id` | `int` | Optional | Identification of the Acquirer.<br>Restrict to the Acquirer if present. |
| `amount_value` | `float` | Optional | Value of an amount.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `host_transaction_id` | [`HostTransactionId`](../../doc/models/host-transaction-id.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.original_poi_transaction import OriginalPoiTransaction
from adyen.models.poi_transaction_id import PoiTransactionId

original_poi_transaction = OriginalPoiTransaction(
    sale_id='SaleID2',
    poiid='POIID6',
    poi_transaction_id=PoiTransactionId(
        transaction_id='TransactionID2',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reuse_card_data_flag=True,
    approval_code='ApprovalCode4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

