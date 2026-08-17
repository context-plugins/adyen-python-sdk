
# Amazon Pay

## Structure

`AmazonPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amazon_pay_token` | `str` | Optional | This is the `amazonPayToken` that you obtained from the [Get Checkout Session](https://amazon-pay-acquirer-guide.s3-eu-west-1.amazonaws.com/v1/amazon-pay-api-v2/checkout-session.html#get-checkout-session) response. This token is used for API only integration specifically. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `checkout_session_id` | `str` | Optional | The `checkoutSessionId` is used to identify the checkout session at the Amazon Pay side. This field is required only for drop-in and components integration, where it replaces the amazonPayToken. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type4Enum`](../../doc/models/type-4-enum.md) | Optional | **amazonpay**<br><br>**Default**: `"amazonpay"` |

## Example

```python
from adyen.models.amazon_pay import AmazonPay
from adyen.models.type_4_enum import Type4Enum

amazon_pay = AmazonPay(
    amazon_pay_token='amazonPayToken6',
    checkout_attempt_id='checkoutAttemptId4',
    checkout_session_id='checkoutSessionId8',
    sdk_data='sdkData2',
    mtype=Type4Enum.AMAZONPAY
)
```

