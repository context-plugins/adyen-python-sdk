
# Order Item

## Structure

`OrderItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the product. |
| `installments` | `int` | Optional | The number of installments for the specified product `id`. |
| `name` | `str` | Optional | The name of the product. |
| `quantity` | `int` | Optional | The number of items with the specified product `id` included in the order. |

## Example

```python
from adyen.models.order_item import OrderItem

order_item = OrderItem(
    id='id2',
    installments=222,
    name='name2',
    quantity=40
)
```

