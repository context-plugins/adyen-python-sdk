
# Terminal Order Request

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

## Example

```python
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
            quantity=22
        ),
        OrderItem(
            id='id8',
            installments=204,
            name='name8',
            quantity=22
        )
    ],
    order_type='orderType8',
    shipping_location_id='shippingLocationId2'
)
```

