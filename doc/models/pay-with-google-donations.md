
# Pay with Google Donations

## Structure

`PayWithGoogleDonations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSourceEnum`](../../doc/models/funding-source-enum.md) | Optional | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |
| `google_pay_token` | `str` | Required | The `token` that you obtained from the [Google Pay API](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) `PaymentData` response.<br><br>**Constraints**: *Maximum Length*: `5000` |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `three_ds_2_sdk_version` | `str` | Optional | Required for mobile integrations. Version of the 3D Secure 2 mobile SDK.<br><br>**Constraints**: *Maximum Length*: `12` |
| `mtype` | [`Type26Enum`](../../doc/models/type-26-enum.md) | Optional | **paywithgoogle**<br><br>**Default**: `"paywithgoogle"` |

## Example

```python
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.pay_with_google_donations import PayWithGoogleDonations
from adyen.models.type_26_enum import Type26Enum

pay_with_google_donations = PayWithGoogleDonations(
    google_pay_token='googlePayToken4',
    checkout_attempt_id='checkoutAttemptId8',
    funding_source=FundingSourceEnum.PREPAID,
    recurring_detail_reference='recurringDetailReference2',
    sdk_data='sdkData8',
    stored_payment_method_id='storedPaymentMethodId6',
    mtype=Type26Enum.PAYWITHGOOGLE
)
```

