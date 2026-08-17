
# Paginated Get Card Order Response

## Structure

`PaginatedGetCardOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_orders` | [`List[CardOrder]`](../../doc/models/card-order.md) | Optional | Contains objects with information about card orders. |
| `has_next` | `bool` | Required | Indicates whether there are more items on the next page. |
| `has_previous` | `bool` | Required | Indicates whether there are more items on the previous page. |

## Example

```python
import dateutil.parser

from adyen.models.card_order import CardOrder
from adyen.models.paginated_get_card_order_response import PaginatedGetCardOrderResponse

paginated_get_card_order_response = PaginatedGetCardOrderResponse(
    has_next=False,
    has_previous=False,
    card_orders=[
        CardOrder(
            begin_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            card_manufacturing_profile_id='cardManufacturingProfileId6',
            closed_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            end_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id2'
        ),
        CardOrder(
            begin_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            card_manufacturing_profile_id='cardManufacturingProfileId6',
            closed_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            end_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id2'
        ),
        CardOrder(
            begin_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            card_manufacturing_profile_id='cardManufacturingProfileId6',
            closed_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            end_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id2'
        )
    ]
)
```

