
# Transaction ID Type

Identification of a transaction for the Sale System or the POI System.

## Structure

`TransactionIDType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Required | Unique identification of a transaction to identify the transaction on<br>the Sale System (e.g. ticket number), or the POI System.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `time_stamp` | `datetime` | Required | Date and time of a transaction for the Sale System, the POI System or the Acquirer.<br>Ensures the uniqueness of a transaction and indicates the time when the event<br>occurs in the EventNotification message. |

## Example

```python
import dateutil.parser

from adyen.models.transaction_id_type import TransactionIDType

transaction_id_type = TransactionIDType(
    transaction_id='TransactionID0',
    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

