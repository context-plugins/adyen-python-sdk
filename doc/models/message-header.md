
# Message Header

Message header of the Sale to POI protocol message.
It conveys Information related to the Sale to POI protocol management.

## Structure

`MessageHeader`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `protocol_version` | `str` | Optional | If MessageCategory is Login or Diagnosis.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `message_class` | [`MessageClass1Enum`](../../doc/models/message-class-1-enum.md) | Required | Class of the message.<br>Possible values:<br><br>* **Device**<br>* **Event**<br>* **Service** |
| `message_category` | [`MessageCategory1Enum`](../../doc/models/message-category-1-enum.md) | Required | Category of message.<br>Possible values:<br><br>* **Abort**<br>* **Admin**<br>* **BalanceInquiry**<br>* **Batch**<br>* **CardAcquisition**<br>* **CardReaderInit**<br>* **CardReaderPowerOff**<br>* **Diagnosis**<br>* **Display**<br>* **EnableService**<br>* **Event**<br>* **GetTotals**<br>* **Input**<br>* **InputUpdate**<br>* **Login**<br>* **Logout**<br>* **Loyalty**<br>* **None**<br>* **PIN**<br>* **Payment**<br>* **Print**<br>* **Reconciliation**<br>* **Reversal**<br>* **Sound**<br>* **StoredValue**<br>* **TransactionStatus**<br>* **Transmit** |
| `message_type` | [`MessageType1Enum`](../../doc/models/message-type-1-enum.md) | Required | Type of message of the Sale to POI protocol.<br>Possible values:<br><br>* **Notification**<br>* **Request**<br>* **Response** |
| `service_id` | `str` | Optional | Identification of a message pair, which processes a transaction.<br>Required if Service or Event MessageClass message or if Device MessageClass and request from POI or response from Sale.<br><br>**Constraints**: *Pattern*: `^.{1,10}$` |
| `device_id` | `str` | Optional | Identification of a device message pair.<br>If Device MessageClass.<br><br>**Constraints**: *Pattern*: `^.{1,10}$` |
| `sale_id` | `str` | Required | Identification of a Sale System or a Sale Terminal for the Sale to POI protocol.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `poiid` | `str` | Required | Identification of a POI System or a POI Terminal for the Sale to POI protocol.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.message_category_1_enum import MessageCategory1Enum
from adyen.models.message_class_1_enum import MessageClass1Enum
from adyen.models.message_header import MessageHeader
from adyen.models.message_type_1_enum import MessageType1Enum

message_header = MessageHeader(
    message_class=MessageClass1Enum.SERVICE,
    message_category=MessageCategory1Enum.STOREDVALUE,
    message_type=MessageType1Enum.RESPONSE,
    sale_id='SaleID8',
    poiid='POIID6',
    protocol_version='ProtocolVersion8',
    service_id='ServiceID4',
    device_id='DeviceID8'
)
```

