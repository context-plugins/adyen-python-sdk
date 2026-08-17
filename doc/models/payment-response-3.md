
# Payment Response 3

Only returned for `resultCode`: **Authorised**.
Details about the payment method used in the transaction.

## Structure

`PaymentResponse3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Optional | The card brand that the shopper used to pay. Only returned if `paymentMethod.type` is **scheme**. |
| `mtype` | `str` | Optional | The `paymentMethod.type` value used in the request. |

## Example

```python
from adyen.models.payment_response_3 import PaymentResponse3

payment_response_3 = PaymentResponse3(
    brand='brand8',
    mtype='type6'
)
```

