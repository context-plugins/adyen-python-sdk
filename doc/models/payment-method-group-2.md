
# Payment Method Group 2

The group where this payment method belongs to.

## Structure

`PaymentMethodGroup2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the group. |
| `payment_method_data` | `str` | Optional | Echo data to be used if the payment method is displayed as part of this group. |
| `mtype` | `str` | Optional | The unique code of the group. |

## Example

```python
from adyen.models.payment_method_group_2 import PaymentMethodGroup2

payment_method_group_2 = PaymentMethodGroup2(
    name='name2',
    payment_method_data='paymentMethodData4',
    mtype='type8'
)
```

