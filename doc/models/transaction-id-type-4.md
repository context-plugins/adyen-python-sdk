
# Transaction ID Type 4

Unique identification of a POI transaction for a POI.
Absent if SaleReferenceID is sufficient to identify the transaction.

## Structure

`TransactionIDType4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Required | Unique identification of a transaction to identify the transaction on<br>the Sale System (e.g. ticket number), or the POI System.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `time_stamp` | `datetime` | Required | Date and time of a transaction for the Sale System, the POI System or the Acquirer.<br>Ensures the uniqueness of a transaction and indicates the time when the event<br>occurs in the EventNotification message. |

## Example

```python
import dateutil.parser

from adyen.models.transaction_id_type_4 import TransactionIDType4

transaction_id_type_4 = TransactionIDType4(
    transaction_id='TransactionID4',
    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

