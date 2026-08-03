
# Terminal Order Request

*This model accepts additional fields of type Any.*

## Structure

`TerminalOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_entity_id` | `str` | Optional | The identification of the billing entity to use for the order.<br><br>> When ordering products in Brazil, you do not need to include the `billingEntityId` in the request. |
| `customer_order_reference` | `str` | Optional | The merchant-defined purchase order reference. |
| `items` | [`List[OrderItem]`](../../doc/models/order-item.md) | Optional | The products included in the order. |
| `order_type` | `str` | Optional | Type of order |
| `shipping_location_id` | `str` | Optional | The identification of the shipping location to use for the order. |
| `tax_id` | `str` | Optional | The tax number of the billing entity. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.order_item import OrderItem
from adyen.models.terminal_order_request import TerminalOrderRequest

terminal_order_request = TerminalOrderRequest(
    billing_entity_id='billingEntityId4',
    customer_order_reference='customerOrderReference6',
    items=[
        OrderItem(
            id='id8',
            installments=204,
            name='name8',
            quantity=22,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        OrderItem(
            id='id8',
            installments=204,
            name='name8',
            quantity=22,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    order_type='orderType8',
    shipping_location_id='shippingLocationId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

