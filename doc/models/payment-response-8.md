
# Payment Response 8

## Structure

`PaymentResponse8`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Optional | The card brand that the shopper used to pay. Only returned if `paymentMethod.type` is **scheme**. |
| `mtype` | `str` | Optional | The `paymentMethod.type` value used in the request. |

## Example

```python
from adyen.models.payment_response_8 import PaymentResponse8

payment_response_8 = PaymentResponse8(
    brand='brand2',
    mtype='type2'
)
```

