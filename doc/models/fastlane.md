
# Fastlane

## Structure

`Fastlane`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `fastlane_data` | `str` | Required | The encoded fastlane data blob |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | `str` | Required, Constant | **fastlane**<br><br>**Value**: `"fastlane"` |

## Example

```python
from adyen.models.fastlane import Fastlane

fastlane = Fastlane(
    fastlane_data='fastlaneData6',
    checkout_attempt_id='checkoutAttemptId8',
    recurring_detail_reference='recurringDetailReference2',
    sdk_data='sdkData8',
    stored_payment_method_id='storedPaymentMethodId6'
)
```

