
# Payment Response 3

Only returned for `resultCode`: **Authorised**.
Details about the payment method used in the transaction.

*This model accepts additional fields of type Any.*

## Structure

`PaymentResponse3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Optional | The card brand that the shopper used to pay. Only returned if `paymentMethod.type` is **scheme**. |
| `mtype` | `str` | Optional | The `paymentMethod.type` value used in the request. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_response_3 import PaymentResponse3

payment_response_3 = PaymentResponse3(
    brand='brand8',
    mtype='type6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

