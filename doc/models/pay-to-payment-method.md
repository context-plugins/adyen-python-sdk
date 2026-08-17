
# Pay to Payment Method

## Structure

`PayToPaymentMethod`

## Inherits From

[`ShopperIdPaymentMethod`](../../doc/models/shopper-id-payment-method.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shopper_reference` | `str` | Optional | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `256` |

## Example

```python
from adyen.models.shopper_id_payment_method import PayToPaymentMethod

pay_to_payment_method = PayToPaymentMethod(
    shopper_reference='shopperReference6',
    mtype='payTo'
)
```

