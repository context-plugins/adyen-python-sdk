
# Shopper Id Payment Method

## Structure

`ShopperIdPaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |

## Example

```python
from adyen.models.shopper_id_payment_method import UPIPaymentMethod

shopper_id_payment_method = UPIPaymentMethod(
    virtual_payment_address='virtualPaymentAddress4',
    mtype='upi_collect'
)
```

