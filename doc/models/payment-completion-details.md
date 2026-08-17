
# Payment Completion Details

## Structure

`PaymentCompletionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `md` | `str` | Optional | A payment session identifier returned by the card issuer.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `pa_req` | `str` | Optional | (3D) Payment Authentication Request data for the card issuer.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `pa_res` | `str` | Optional | (3D) Payment Authentication Response data by the card issuer.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `authorization_token` | `str` | Optional | - |
| `billing_token` | `str` | Optional | PayPal-generated token for recurring payments. |
| `cupsecureplus_smscode` | `str` | Optional | The SMS verification code collected from the shopper. |
| `facilitator_access_token` | `str` | Optional | PayPal-generated third party access token. |
| `one_time_passcode` | `str` | Optional | A random number sent to the mobile phone number of the shopper to verify the payment. |
| `order_id` | `str` | Optional | PayPal-assigned ID for the order. |
| `payer_id` | `str` | Optional | PayPal-assigned ID for the payer (shopper). |
| `payload` | `str` | Optional | Payload appended to the `returnURL` as a result of the redirect.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `payment_id` | `str` | Optional | PayPal-generated ID for the payment. |
| `payment_status` | `str` | Optional | Value passed from the WeChat MiniProgram `wx.requestPayment` **complete** callback. Possible values: any value starting with `requestPayment:`. |
| `redirect_result` | `str` | Optional | The result of the redirect as appended to the `returnURL`.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `result_code` | `str` | Optional | Value you received from the WeChat Pay SDK. |
| `return_url_query_string` | `str` | Optional | The query string as appended to the `returnURL` when using direct issuer links .<br><br>**Constraints**: *Maximum Length*: `20000` |
| `three_ds_result` | `str` | Optional | Base64-encoded string returned by the Component after the challenge flow. It contains the following parameters: `transStatus`, `authorisationToken`.<br><br>**Constraints**: *Maximum Length*: `50000` |
| `threeds_2_challenge_result` | `str` | Optional | Base64-encoded string returned by the Component after the challenge flow. It contains the following parameter: `transStatus`.<br><br>**Constraints**: *Maximum Length*: `50000` |
| `threeds_2_fingerprint` | `str` | Optional | Base64-encoded string returned by the Component after the challenge flow. It contains the following parameter: `threeDSCompInd`.<br><br>**Constraints**: *Maximum Length*: `100000` |
| `vault_token` | `str` | Optional | PayPalv2-generated token for recurring payments. |

## Example

```python
from adyen.models.payment_completion_details import PaymentCompletionDetails

payment_completion_details = PaymentCompletionDetails(
    md='MD0',
    pa_req='PaReq6',
    pa_res='PaRes6',
    authorization_token='authorization_token0',
    billing_token='billingToken8'
)
```

