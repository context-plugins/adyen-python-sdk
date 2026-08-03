
# Payment Details Request 1

*This model accepts additional fields of type Any.*

## Structure

`PaymentDetailsRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_data` | [`DetailsRequestAuthenticationData`](../../doc/models/details-request-authentication-data.md) | Optional | - |
| `details` | [`PaymentCompletionDetails`](../../doc/models/payment-completion-details.md) | Required | - |
| `payment_data` | `str` | Optional | Encoded payment data. For [authorizing a payment after using 3D Secure 2 Authentication-only](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only/#authorise-the-payment-with-adyen):<br><br>If you received `resultCode`: **AuthenticationNotRequired** in the `/payments` response, use the `threeDSPaymentData` from the same response.<br><br>If you received `resultCode`: **AuthenticationFinished** in the `/payments` response, use the `action.paymentData` from the same response.<br><br>**Constraints**: *Maximum Length*: `200000` |
| `three_ds_authentication_only` | `bool` | Optional | Change the `authenticationOnly` indicator originally set in the `/payments` request. Only needs to be set if you want to modify the value set previously. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.details_request_authentication_data import DetailsRequestAuthenticationData
from adyen.models.payment_completion_details import PaymentCompletionDetails
from adyen.models.payment_details_request_1 import PaymentDetailsRequest1

payment_details_request_1 = PaymentDetailsRequest1(
    details=PaymentCompletionDetails(
        md='MD4',
        pa_req='PaReq0',
        pa_res='PaRes0',
        authorization_token='authorization_token4',
        billing_token='billingToken2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    authentication_data=DetailsRequestAuthenticationData(
        authentication_only=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    payment_data='paymentData2',
    three_ds_authentication_only=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

