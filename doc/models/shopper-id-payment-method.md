
# Shopper Id Payment Method

*This model accepts additional fields of type Any.*

## Structure

`ShopperIdPaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.shopper_id_payment_method import UpiPaymentMethod

shopper_id_payment_method = UpiPaymentMethod(
    virtual_payment_address='virtualPaymentAddress4',
    mtype='upi_collect',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

