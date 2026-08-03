
# Delivery Method

*This model accepts additional fields of type Any.*

## Structure

`DeliveryMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `description` | `str` | Optional | The name of the delivery method as shown to the shopper. |
| `reference` | `str` | Optional | The reference of the delivery method. |
| `selected` | `bool` | Optional | If you display the PayPal lightbox with delivery methods, set to **true** for the delivery method that is selected. Only one delivery method can be selected at a time. |
| `mtype` | [`Type211`](../../doc/models/type-211.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.delivery_method import DeliveryMethod
from adyen.models.type_211 import Type211

delivery_method = DeliveryMethod(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    description='description6',
    reference='reference8',
    selected=False,
    mtype=Type211.SHIPPING,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

