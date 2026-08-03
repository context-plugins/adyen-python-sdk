
# Terminal Order

*This model accepts additional fields of type Any.*

## Structure

`TerminalOrder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_entity` | [`BillingEntity`](../../doc/models/billing-entity.md) | Optional | - |
| `customer_order_reference` | `str` | Optional | The merchant-defined purchase order number. This will be printed on the packing list. |
| `id` | `str` | Optional | The unique identifier of the order. |
| `items` | [`List[OrderItem]`](../../doc/models/order-item.md) | Optional | The products included in the order. |
| `order_date` | `str` | Optional | The date and time that the order was placed, in UTC ISO 8601 format. For example, "2011-12-03T10:15:30Z". |
| `shipping_location` | [`ShippingLocation`](../../doc/models/shipping-location.md) | Optional | - |
| `status` | `str` | Optional | The processing status of the order. |
| `tracking_url` | `str` | Optional | The URL, provided by the carrier company, where the shipment can be tracked. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_6 import Address6
from adyen.models.billing_entity import BillingEntity
from adyen.models.order_item import OrderItem
from adyen.models.terminal_order import TerminalOrder

terminal_order = TerminalOrder(
    billing_entity=BillingEntity(
        address=Address6(
            city='city6',
            company_name='companyName8',
            country='country0',
            postal_code='postalCode8',
            state_or_province='stateOrProvince4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        email='email0',
        id='id6',
        name='name6',
        tax_id='taxId2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    customer_order_reference='customerOrderReference8',
    id='id6',
    items=[
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
    order_date='orderDate6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

