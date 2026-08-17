
# Apple Pay Donations

## Structure

`ApplePayDonations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apple_pay_token` | `str` | Required | The stringified and base64 encoded `paymentData` you retrieved from the Apple framework.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSourceEnum`](../../doc/models/funding-source-enum.md) | Optional | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type7Enum`](../../doc/models/type-7-enum.md) | Optional | **applepay**<br><br>**Default**: `"applepay"` |

## Example

```python
from adyen.models.apple_pay_donations import ApplePayDonations
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.type_7_enum import Type7Enum

apple_pay_donations = ApplePayDonations(
    apple_pay_token='applePayToken4',
    checkout_attempt_id='checkoutAttemptId8',
    funding_source=FundingSourceEnum.CREDIT,
    recurring_detail_reference='recurringDetailReference2',
    sdk_data='sdkData8',
    stored_payment_method_id='storedPaymentMethodId6',
    mtype=Type7Enum.APPLEPAY
)
```

