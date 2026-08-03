
# Terminal Orders Response

*This model accepts additional fields of type Any.*

## Structure

`TerminalOrdersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[TerminalOrder]`](../../doc/models/terminal-order.md) | Optional | List of orders for payment terminal packages and parts. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_6 import Address6
from adyen.models.billing_entity import BillingEntity
from adyen.models.order_item import OrderItem
from adyen.models.terminal_order import TerminalOrder
from adyen.models.terminal_orders_response import TerminalOrdersResponse

terminal_orders_response = TerminalOrdersResponse(
    data=[
        TerminalOrder(
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
            customer_order_reference='customerOrderReference2',
            id='id0',
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
            order_date='orderDate0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        TerminalOrder(
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
            customer_order_reference='customerOrderReference2',
            id='id0',
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
            order_date='orderDate0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

