
# Checkout Delegated Authentication Action

## Structure

`CheckoutDelegatedAuthenticationAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_token` | `str` | Optional | A token needed to authorise a payment. |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `token` | `str` | Optional | A token to pass to the delegatedAuthentication component. |
| `mtype` | `str` | Required, Constant | **delegatedAuthentication**<br><br>**Value**: `"delegatedAuthentication"` |
| `url` | `str` | Optional | Specifies the URL to redirect to. |

## Example

```python
from adyen.models.checkout_delegated_authentication_action import CheckoutDelegatedAuthenticationAction

checkout_delegated_authentication_action = CheckoutDelegatedAuthenticationAction(
    authorisation_token='authorisationToken8',
    payment_data='paymentData6',
    payment_method_type='paymentMethodType6',
    token='token8',
    url='url8'
)
```

