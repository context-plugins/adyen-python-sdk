
# Checkout Three DS 2 Action

## Structure

`CheckoutThreeDS2Action`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_token` | `str` | Optional | A token needed to authorise a payment. |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `subtype` | `str` | Optional | A subtype of the token. |
| `token` | `str` | Optional | A token to pass to the 3DS2 Component to get the fingerprint. |
| `mtype` | `str` | Required, Constant | **threeDS2**<br><br>**Value**: `"threeDS2"` |
| `url` | `str` | Optional | Specifies the URL to redirect to. |

## Example

```python
from adyen.models.checkout_three_ds_2_action import CheckoutThreeDS2Action

checkout_three_ds_2_action = CheckoutThreeDS2Action(
    authorisation_token='authorisationToken2',
    payment_data='paymentData0',
    payment_method_type='paymentMethodType0',
    subtype='subtype0',
    token='token8'
)
```

