
# Card Order Item Delivery Status 1

Contains information about the status of the PIN delivery.

*This model accepts additional fields of type Any.*

## Structure

`CardOrderItemDeliveryStatus1`

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

from adyen.models.card_order_item_delivery_status_1 import CardOrderItemDeliveryStatus1
from adyen.models.status_7 import Status7

card_order_item_delivery_status_1 = CardOrderItemDeliveryStatus1(
    error_message='errorMessage4',
    status=Status7.CREATED,
    tracking_number='trackingNumber4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

