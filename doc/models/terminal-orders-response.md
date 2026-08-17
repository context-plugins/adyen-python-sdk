
# Terminal Orders Response

## Structure

`TerminalOrdersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[TerminalOrder]`](../../doc/models/terminal-order.md) | Optional | List of orders for payment terminal packages and parts. |

## Example

```python
from adyen.models.address_11 import Address11
from adyen.models.billing_entity_1 import BillingEntity1
from adyen.models.order_item import OrderItem
from adyen.models.terminal_order import TerminalOrder
from adyen.models.terminal_orders_response import TerminalOrdersResponse

terminal_orders_response = TerminalOrdersResponse(
    data=[
        TerminalOrder(
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
            customer_order_reference='customerOrderReference2',
            id='id0',
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
                ),
                OrderItem(
                    id='id8',
                    installments=204,
                    name='name8',
                    quantity=22
                )
            ],
            order_date='orderDate0'
        ),
        TerminalOrder(
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
            customer_order_reference='customerOrderReference2',
            id='id0',
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
                ),
                OrderItem(
                    id='id8',
                    installments=204,
                    name='name8',
                    quantity=22
                )
            ],
            order_date='orderDate0'
        )
    ]
)
```

