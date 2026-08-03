
# Card Order Item Delivery Status 3

The status of the card delivery.

Possible values: **created**, **rejected**, **processing**, **produced**, **shipped**, **delivered**, **notApplicable**, **unknown**.

*This model accepts additional fields of type Any.*

## Structure

`CardOrderItemDeliveryStatus3`

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

from adyen.models.card_order_item_delivery_status_3 import CardOrderItemDeliveryStatus3
from adyen.models.status_7 import Status7

card_order_item_delivery_status_3 = CardOrderItemDeliveryStatus3(
    error_message='errorMessage0',
    status=Status7.CREATED,
    tracking_number='trackingNumber0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

