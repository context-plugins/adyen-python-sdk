
# UPI Payment Method

## Structure

`UPIPaymentMethod`

## Inherits From

[`ShopperIdPaymentMethod`](../../doc/models/shopper-id-payment-method.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `virtual_payment_address` | `str` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `256` |

## Example

```python
from adyen.models.shopper_id_payment_method import UPIPaymentMethod

upi_payment_method = UPIPaymentMethod(
    virtual_payment_address='virtualPaymentAddress0',
    mtype='upi_collect'
)
```

