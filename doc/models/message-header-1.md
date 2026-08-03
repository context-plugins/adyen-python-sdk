
# Message Header 1

*This model accepts additional fields of type Any.*

## Structure

`MessageHeader1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `protocol_version` | `str` | Optional | If MessageCategory is Login or Diagnosis.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `message_class` | [`MessageClass1`](../../doc/models/message-class-1.md) | Required | - |
| `message_category` | [`MessageCategory1`](../../doc/models/message-category-1.md) | Required | - |
| `message_type` | [`MessageType1`](../../doc/models/message-type-1.md) | Required | - |
| `service_id` | `str` | Optional | Identification of a message pair, which processes a transaction.<br>Required if Service or Event MessageClass message or if Device MessageClass and request from POI or response from Sale.<br><br>**Constraints**: *Pattern*: `^.{1,10}$` |
| `device_id` | `str` | Optional | Identification of a device message pair.<br>If Device MessageClass.<br><br>**Constraints**: *Pattern*: `^.{1,10}$` |
| `sale_id` | `str` | Required | Identification of a Sale System or a Sale Terminal for the Sale to POI protocol.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `poiid` | `str` | Required | Identification of a POI System or a POI Terminal for the Sale to POI protocol.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.message_category_1 import MessageCategory1
from adyen.models.message_class_1 import MessageClass1
from adyen.models.message_header_1 import MessageHeader1
from adyen.models.message_type_1 import MessageType1

message_header_1 = MessageHeader1(
    message_class=MessageClass1.EVENT,
    message_category=MessageCategory1.LOGIN,
    message_type=MessageType1.RESPONSE,
    sale_id='SaleID2',
    poiid='POIID8',
    protocol_version='ProtocolVersion6',
    service_id='ServiceID0',
    device_id='DeviceID2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

