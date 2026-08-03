
# Message Reference 2

Identification of a previous POI transaction.
Present if it contains any data.

*This model accepts additional fields of type Any.*

## Structure

`MessageReference2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_category` | [`MessageCategory2`](../../doc/models/message-category-2.md) | Optional | - |
| `service_id` | `str` | Optional | Identification of a message pair, which processes a transaction.<br><br>**Constraints**: *Pattern*: `^.{1,10}$` |
| `device_id` | `str` | Optional | Identification of a device message pair.<br><br>**Constraints**: *Pattern*: `^.{1,10}$` |
| `sale_id` | `str` | Optional | Identification of a Sale System or a Sale Terminal for the Sale to POI protocol.<br>default MessageHeader.SaleID.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `poiid` | `str` | Optional | Identification of a POI System or a POI Terminal for the Sale to POI protocol.<br>Default `MessageHeader.POIID`.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.message_category_2 import MessageCategory2
from adyen.models.message_reference_2 import MessageReference2

message_reference_2 = MessageReference2(
    message_category=MessageCategory2.DISPLAY,
    service_id='ServiceID8',
    device_id='DeviceID0',
    sale_id='SaleID0',
    poiid='POIID6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

