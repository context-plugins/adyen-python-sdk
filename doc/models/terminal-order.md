
# Terminal Order

## Structure

`TerminalOrder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_entity` | [`BillingEntity1`](../../doc/models/billing-entity-1.md) | Optional | The details of the entity that the order is billed to. |
| `customer_order_reference` | `str` | Optional | The merchant-defined purchase order number. This will be printed on the packing list. |
| `id` | `str` | Optional | The unique identifier of the order. |
| `items` | [`List[OrderItem]`](../../doc/models/order-item.md) | Optional | The products included in the order. |
| `order_date` | `str` | Optional | The date and time that the order was placed, in UTC ISO 8601 format. For example, "2011-12-03T10:15:30Z". |
| `shipping_location` | [`ShippingLocation1`](../../doc/models/shipping-location-1.md) | Optional | The details of the location where the order is shipped to. |
| `status` | `str` | Optional | The processing status of the order. |
| `tracking_url` | `str` | Optional | The URL, provided by the carrier company, where the shipment can be tracked. |

## Example

```python
from adyen.models.address_11 import Address11
from adyen.models.billing_entity_1 import BillingEntity1
from adyen.models.order_item import OrderItem
from adyen.models.terminal_order import TerminalOrder

terminal_order = TerminalOrder(
    billing_entity=BillingEntity1(
        address=Address11(
            city='city6',
            company_name='companyName8',
            country='country0',
            postal_code='postalCode8',
            state_or_province='stateOrProvince4'
        ),
        email='email0',
        id='id6',
        name='name6',
        tax_id='taxId2'
    ),
    customer_order_reference='customerOrderReference8',
    id='id6',
    items=[
        OrderItem(
            id='id8',
            installments=204,
            name='name8',
            quantity=22
        )
    ],
    order_date='orderDate6'
)
```

