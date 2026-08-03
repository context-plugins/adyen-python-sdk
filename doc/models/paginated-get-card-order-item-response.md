
# Paginated Get Card Order Item Response

*This model accepts additional fields of type Any.*

## Structure

`PaginatedGetCardOrderItemResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[CardOrderItem]`](../../doc/models/card-order-item.md) | Required | List of card order items in the card order batch. |
| `has_next` | `bool` | Required | Indicates whether there are more items on the next page. |
| `has_previous` | `bool` | Required | Indicates whether there are more items on the previous page. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.card_order_item import CardOrderItem
from adyen.models.card_order_item_delivery_status import CardOrderItemDeliveryStatus
from adyen.models.paginated_get_card_order_item_response import PaginatedGetCardOrderItemResponse
from adyen.models.status_7 import Status7

paginated_get_card_order_item_response = PaginatedGetCardOrderItemResponse(
    data=[
        CardOrderItem(
            balance_platform='balancePlatform2',
            card=CardOrderItemDeliveryStatus(
                error_message='errorMessage4',
                status=Status7.SHIPPED,
                tracking_number='trackingNumber4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            card_order_item_id='cardOrderItemId6',
            creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    has_next=False,
    has_previous=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

