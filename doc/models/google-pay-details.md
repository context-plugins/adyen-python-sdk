
# Google Pay Details

## Structure

`GooglePayDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSourceEnum`](../../doc/models/funding-source-enum.md) | Optional | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |
| `google_pay_card_network` | `str` | Optional | The selected payment card network. |
| `google_pay_token` | `str` | Required | The `token` that you obtained from the [Google Pay API](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) `PaymentData` response.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `three_ds_2_sdk_version` | `str` | Optional | Required for mobile integrations. Version of the 3D Secure 2 mobile SDK.<br><br>**Constraints**: *Maximum Length*: `12` |
| `mtype` | [`Type24Enum`](../../doc/models/type-24-enum.md) | Optional | **googlepay**, **paywithgoogle**<br><br>**Default**: `"googlepay"` |

## Example

```python
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.google_pay_details import GooglePayDetails
from adyen.models.type_24_enum import Type24Enum

google_pay_details = GooglePayDetails(
    google_pay_token='googlePayToken2',
    checkout_attempt_id='checkoutAttemptId6',
    funding_source=FundingSourceEnum.PREPAID,
    google_pay_card_network='googlePayCardNetwork6',
    recurring_detail_reference='recurringDetailReference0',
    sdk_data='sdkData0',
    mtype=Type24Enum.GOOGLEPAY
)
```

