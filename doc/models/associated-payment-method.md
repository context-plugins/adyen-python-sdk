
# Associated Payment Method

## Structure

`AssociatedPaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Required | Indicates whether the payment method is enabled (**true**) or disabled (**false**). |
| `id` | `str` | Required | The identifier of the payment method. |
| `mtype` | `str` | Required | Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api). |

## Example

```python
from adyen.models.associated_payment_method import AssociatedPaymentMethod

associated_payment_method = AssociatedPaymentMethod(
    enabled=False,
    id='id4',
    mtype='type6'
)
```

