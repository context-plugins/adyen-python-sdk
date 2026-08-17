
# Payment Method Group

## Structure

`PaymentMethodGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the group. |
| `payment_method_data` | `str` | Optional | Echo data to be used if the payment method is displayed as part of this group. |
| `mtype` | `str` | Optional | The unique code of the group. |

## Example

```python
from adyen.models.payment_method_group import PaymentMethodGroup

payment_method_group = PaymentMethodGroup(
    name='name8',
    payment_method_data='paymentMethodData2',
    mtype='type2'
)
```

