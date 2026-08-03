
# Pay to Payment Method

*This model accepts additional fields of type Any.*

## Structure

`PayToPaymentMethod`

## Inherits From

[`ShopperIdPaymentMethod`](../../doc/models/shopper-id-payment-method.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shopper_reference` | `str` | Optional | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `256` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.shopper_id_payment_method import PayToPaymentMethod

pay_to_payment_method = PayToPaymentMethod(
    shopper_reference='shopperReference6',
    mtype='payTo',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

