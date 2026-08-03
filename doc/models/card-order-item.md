
# Card Order Item

*This model accepts additional fields of type Any.*

## Structure

`CardOrderItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform` | `str` | Optional | The unique identifier of the balance platform. |
| `card` | [`CardOrderItemDeliveryStatus`](../../doc/models/card-order-item-delivery-status.md) | Optional | - |
| `card_order_item_id` | `str` | Optional | The unique identifier of the card order item. |
| `creation_date` | `datetime` | Optional | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**. |
| `id` | `str` | Optional, Read-only | The ID of the resource. |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument related to the card order item. |
| `pin` | [`CardOrderItemDeliveryStatus`](../../doc/models/card-order-item-delivery-status.md) | Optional | - |
| `shipping_method` | `str` | Optional | The shipping method used to deliver the card or the PIN. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.card_order_item import CardOrderItem
from adyen.models.card_order_item_delivery_status import CardOrderItemDeliveryStatus
from adyen.models.status_7 import Status7

card_order_item = CardOrderItem(
    balance_platform='balancePlatform6',
    card=CardOrderItemDeliveryStatus(
        error_message='errorMessage4',
        status=Status7.SHIPPED,
        tracking_number='trackingNumber4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card_order_item_id='cardOrderItemId0',
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

