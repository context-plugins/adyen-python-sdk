
# Card Order Item Delivery Status

*This model accepts additional fields of type Any.*

## Structure

`CardOrderItemDeliveryStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `str` | Optional | An error message. |
| `status` | [`Status7`](../../doc/models/status-7.md) | Optional | - |
| `tracking_number` | `str` | Optional | The tracking number of the PIN delivery. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_order_item_delivery_status import CardOrderItemDeliveryStatus
from adyen.models.status_7 import Status7

card_order_item_delivery_status = CardOrderItemDeliveryStatus(
    error_message='errorMessage2',
    status=Status7.PRODUCED,
    tracking_number='trackingNumber2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

