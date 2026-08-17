
# Card Order Item Delivery Status 3

The status of the card delivery.

Possible values: **created**, **rejected**, **processing**, **produced**, **shipped**, **delivered**, **notApplicable**, **unknown**.

## Structure

`CardOrderItemDeliveryStatus3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `str` | Optional | An error message. |
| `status` | [`Status71Enum`](../../doc/models/status-71-enum.md) | Optional | The status of the PIN delivery. |
| `tracking_number` | `str` | Optional | The tracking number of the PIN delivery. |

## Example

```python
from adyen.models.card_order_item_delivery_status_3 import CardOrderItemDeliveryStatus3
from adyen.models.status_71_enum import Status71Enum

card_order_item_delivery_status_3 = CardOrderItemDeliveryStatus3(
    error_message='errorMessage0',
    status=Status71Enum.CREATED,
    tracking_number='trackingNumber0'
)
```

