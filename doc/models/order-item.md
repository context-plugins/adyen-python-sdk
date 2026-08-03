
# Order Item

*This model accepts additional fields of type Any.*

## Structure

`OrderItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the product. |
| `installments` | `int` | Optional | The number of installments for the specified product `id`. |
| `name` | `str` | Optional | The name of the product. |
| `quantity` | `int` | Optional | The number of items with the specified product `id` included in the order. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.order_item import OrderItem

order_item = OrderItem(
    id='id2',
    installments=222,
    name='name2',
    quantity=40,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

