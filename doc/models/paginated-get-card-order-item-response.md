
# Paginated Get Card Order Item Response

## Structure

`PaginatedGetCardOrderItemResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[CardOrderItem]`](../../doc/models/card-order-item.md) | Required | List of card order items in the card order batch. |
| `has_next` | `bool` | Required | Indicates whether there are more items on the next page. |
| `has_previous` | `bool` | Required | Indicates whether there are more items on the previous page. |

## Example

```python
import dateutil.parser

from adyen.models.card_order_item import CardOrderItem
from adyen.models.card_order_item_delivery_status_3 import CardOrderItemDeliveryStatus3
from adyen.models.paginated_get_card_order_item_response import PaginatedGetCardOrderItemResponse
from adyen.models.status_71_enum import Status71Enum

paginated_get_card_order_item_response = PaginatedGetCardOrderItemResponse(
    data=[
        CardOrderItem(
            balance_platform='balancePlatform2',
            card=CardOrderItemDeliveryStatus3(
                error_message='errorMessage4',
                status=Status71Enum.SHIPPED,
                tracking_number='trackingNumber4'
            ),
            card_order_item_id='cardOrderItemId6',
            creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ],
    has_next=False,
    has_previous=False
)
```

