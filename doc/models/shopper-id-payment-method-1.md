
# Shopper Id Payment Method 1

paymentMethod

*This model accepts additional fields of type Any.*

## Structure

`ShopperIdPaymentMethod1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.shopper_id_payment_method_1 import ShopperIdPaymentMethod1

shopper_id_payment_method_1 = ShopperIdPaymentMethod1(
    mtype='ShopperIdPaymentMethod1',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

