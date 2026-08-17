
# Payment Details

## Structure

`PaymentDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type43Enum`](../../doc/models/type-43-enum.md) | Optional | The payment method type. |

## Example

```python
from adyen.models.payment_details import PaymentDetails
from adyen.models.type_43_enum import Type43Enum

payment_details = PaymentDetails(
    checkout_attempt_id='checkoutAttemptId6',
    sdk_data='sdkData0',
    mtype=Type43Enum.WALLEY_B2B
)
```

