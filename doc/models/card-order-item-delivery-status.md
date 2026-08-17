
# Card Order Item Delivery Status

## Structure

`CardOrderItemDeliveryStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `str` | Optional | An error message. |
| `status` | [`Status71Enum`](../../doc/models/status-71-enum.md) | Optional | The status of the PIN delivery. |
| `tracking_number` | `str` | Optional | The tracking number of the PIN delivery. |

## Example

```python
from adyen.models.card_order_item_delivery_status import CardOrderItemDeliveryStatus
from adyen.models.status_71_enum import Status71Enum

card_order_item_delivery_status = CardOrderItemDeliveryStatus(
    error_message='errorMessage2',
    status=Status71Enum.PRODUCED,
    tracking_number='trackingNumber2'
)
```

