
# Card Order Item

## Structure

`CardOrderItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform` | `str` | Optional | The unique identifier of the balance platform. |
| `card` | [`CardOrderItemDeliveryStatus3`](../../doc/models/card-order-item-delivery-status-3.md) | Optional | The status of the card delivery.<br><br>Possible values: **created**, **rejected**, **processing**, **produced**, **shipped**, **delivered**, **notApplicable**, **unknown**. |
| `card_order_item_id` | `str` | Optional | The unique identifier of the card order item. |
| `creation_date` | `datetime` | Optional | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**. |
| `id` | `str` | Optional, Read-only | The ID of the resource. |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument related to the card order item. |
| `pin` | [`CardOrderItemDeliveryStatus1`](../../doc/models/card-order-item-delivery-status-1.md) | Optional | Contains information about the status of the PIN delivery. |
| `shipping_method` | `str` | Optional | The shipping method used to deliver the card or the PIN. |

## Example

```python
import dateutil.parser

from adyen.models.card_order_item import CardOrderItem
from adyen.models.card_order_item_delivery_status_3 import CardOrderItemDeliveryStatus3
from adyen.models.status_71_enum import Status71Enum

card_order_item = CardOrderItem(
    balance_platform='balancePlatform6',
    card=CardOrderItemDeliveryStatus3(
        error_message='errorMessage4',
        status=Status71Enum.SHIPPED,
        tracking_number='trackingNumber4'
    ),
    card_order_item_id='cardOrderItemId0',
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

