
# Transaction ID Type 3

Reference to the last CardAcquisition, to use the same card.
If the loyalty account ID comes from a previous CardAcquisition.

## Structure

`TransactionIDType3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Required | Unique identification of a transaction to identify the transaction on<br>the Sale System (e.g. ticket number), or the POI System.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `time_stamp` | `datetime` | Required | Date and time of a transaction for the Sale System, the POI System or the Acquirer.<br>Ensures the uniqueness of a transaction and indicates the time when the event<br>occurs in the EventNotification message. |

## Example

```python
import dateutil.parser

from adyen.models.transaction_id_type_3 import TransactionIDType3

transaction_id_type_3 = TransactionIDType3(
    transaction_id='TransactionID0',
    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

