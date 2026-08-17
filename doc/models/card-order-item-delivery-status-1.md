
# Card Order Item Delivery Status 1

Contains information about the status of the PIN delivery.

## Structure

`CardOrderItemDeliveryStatus1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `str` | Optional | An error message. |
| `status` | [`Status71Enum`](../../doc/models/status-71-enum.md) | Optional | The status of the PIN delivery. |
| `tracking_number` | `str` | Optional | The tracking number of the PIN delivery. |

## Example

```python
from adyen.models.card_order_item_delivery_status_1 import CardOrderItemDeliveryStatus1
from adyen.models.status_71_enum import Status71Enum

card_order_item_delivery_status_1 = CardOrderItemDeliveryStatus1(
    error_message='errorMessage4',
    status=Status71Enum.CREATED,
    tracking_number='trackingNumber4'
)
```

