
# Payment Response 1

Details about the payment method used in the transaction.
Only returned if `resultCode` is **Authorised**.

## Structure

`PaymentResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Optional | The card brand that the shopper used to pay. Only returned if `paymentMethod.type` is **scheme**. |
| `mtype` | `str` | Optional | The `paymentMethod.type` value used in the request. |

## Example

```python
from adyen.models.payment_response_1 import PaymentResponse1

payment_response_1 = PaymentResponse1(
    brand='brand6',
    mtype='type8'
)
```

