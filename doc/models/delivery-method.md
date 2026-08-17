
# Delivery Method

## Structure

`DeliveryMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount24`](../../doc/models/amount-24.md) | Optional | The cost of this delivery method. |
| `description` | `str` | Optional | The name of the delivery method as shown to the shopper. |
| `reference` | `str` | Optional | The reference of the delivery method. |
| `selected` | `bool` | Optional | If you display the PayPal lightbox with delivery methods, set to **true** for the delivery method that is selected. Only one delivery method can be selected at a time. |
| `mtype` | [`Type21Enum`](../../doc/models/type-21-enum.md) | Optional | The type of the delivery method. |

## Example

```python
from adyen.models.amount_24 import Amount24
from adyen.models.delivery_method import DeliveryMethod
from adyen.models.type_21_enum import Type21Enum

delivery_method = DeliveryMethod(
    amount=Amount24(
        currency='currency2',
        value=110
    ),
    description='description6',
    reference='reference8',
    selected=False,
    mtype=Type21Enum.SHIPPING
)
```

