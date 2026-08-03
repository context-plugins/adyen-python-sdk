
# Message Reference 3

Identification of a previous POI transaction.
If `Response.Result` is Success.

*This model accepts additional fields of type Any.*

## Structure

`MessageReference3`

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
from adyen.models.message_reference_3 import MessageReference3

message_reference_3 = MessageReference3(
    message_category=MessageCategory2.ENABLESERVICE,
    service_id='ServiceID8',
    device_id='DeviceID4',
    sale_id='SaleID4',
    poiid='POIID0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

