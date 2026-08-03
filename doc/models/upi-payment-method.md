
# Upi Payment Method

*This model accepts additional fields of type Any.*

## Structure

`UpiPaymentMethod`

## Inherits From

[`ShopperIdPaymentMethod`](../../doc/models/shopper-id-payment-method.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `virtual_payment_address` | `str` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `256` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.shopper_id_payment_method import UpiPaymentMethod

upi_payment_method = UpiPaymentMethod(
    virtual_payment_address='virtualPaymentAddress0',
    mtype='upi_collect',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

