
# Message Reference 4

Identification of a previous POI transaction.

## Structure

`MessageReference4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_category` | [`MessageCategory2Enum`](../../doc/models/message-category-2-enum.md) | Optional | Category of message.<br>CardAcquisition, Display, Input, Loyalty, Payment, Print, CardReaderInit, CardReaderPowerOff.<br>Possible values:<br><br>* **Abort**<br>* **Admin**<br>* **BalanceInquiry**<br>* **Batch**<br>* **CardAcquisition**<br>* **CardReaderInit**<br>* **CardReaderPowerOff**<br>* **Diagnosis**<br>* **Display**<br>* **EnableService**<br>* **Event**<br>* **GetTotals**<br>* **Input**<br>* **InputUpdate**<br>* **Login**<br>* **Logout**<br>* **Loyalty**<br>* **None**<br>* **PIN**<br>* **Payment**<br>* **Print**<br>* **Reconciliation**<br>* **Reversal**<br>* **Sound**<br>* **StoredValue**<br>* **TransactionStatus**<br>* **Transmit** |
| `service_id` | `str` | Optional | Identification of a message pair, which processes a transaction.<br><br>**Constraints**: *Pattern*: `^.{1,10}$` |
| `device_id` | `str` | Optional | Identification of a device message pair.<br><br>**Constraints**: *Pattern*: `^.{1,10}$` |
| `sale_id` | `str` | Optional | Identification of a Sale System or a Sale Terminal for the Sale to POI protocol.<br>default MessageHeader.SaleID.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `poiid` | `str` | Optional | Identification of a POI System or a POI Terminal for the Sale to POI protocol.<br>Default `MessageHeader.POIID`.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.message_category_2_enum import MessageCategory2Enum
from adyen.models.message_reference_4 import MessageReference4

message_reference_4 = MessageReference4(
    message_category=MessageCategory2Enum.TRANSACTIONSTATUS,
    service_id='ServiceID0',
    device_id='DeviceID2',
    sale_id='SaleID2',
    poiid='POIID2'
)
```

