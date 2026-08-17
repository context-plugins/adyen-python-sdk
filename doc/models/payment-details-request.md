
# Payment Details Request

## Structure

`PaymentDetailsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_data` | [`DetailsRequestAuthenticationData1`](../../doc/models/details-request-authentication-data-1.md) | Optional | Data for 3DS authentication. |
| `details` | [`PaymentCompletionDetails1`](../../doc/models/payment-completion-details-1.md) | Required | Use this collection to submit the details that were returned as a result of the `/payments` call. |
| `payment_data` | `str` | Optional | Encoded payment data. For [authorizing a payment after using 3D Secure 2 Authentication-only](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only/#authorise-the-payment-with-adyen):<br><br>If you received `resultCode`: **AuthenticationNotRequired** in the `/payments` response, use the `threeDSPaymentData` from the same response.<br><br>If you received `resultCode`: **AuthenticationFinished** in the `/payments` response, use the `action.paymentData` from the same response.<br><br>**Constraints**: *Maximum Length*: `200000` |
| `three_ds_authentication_only` | `bool` | Optional | Change the `authenticationOnly` indicator originally set in the `/payments` request. Only needs to be set if you want to modify the value set previously. |

## Example

```python
from adyen.models.details_request_authentication_data_1 import DetailsRequestAuthenticationData1
from adyen.models.payment_completion_details_1 import PaymentCompletionDetails1
from adyen.models.payment_details_request import PaymentDetailsRequest

payment_details_request = PaymentDetailsRequest(
    details=PaymentCompletionDetails1(
        md='MD4',
        pa_req='PaReq0',
        pa_res='PaRes0',
        authorization_token='authorization_token4',
        billing_token='billingToken2'
    ),
    authentication_data=DetailsRequestAuthenticationData1(
        authentication_only=False
    ),
    payment_data='paymentData6',
    three_ds_authentication_only=False
)
```

