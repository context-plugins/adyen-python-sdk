
# Apple Pay Details

*This model accepts additional fields of type Any.*

## Structure

`ApplePayDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apple_pay_token` | `str` | Required | The stringified and base64 encoded `paymentData` you retrieved from the Apple framework.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSource`](../../doc/models/funding-source.md) | Optional | - |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type71`](../../doc/models/type-71.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.apple_pay_details import ApplePayDetails
from adyen.models.funding_source import FundingSource

apple_pay_details = ApplePayDetails(
    apple_pay_token='applePayToken6',
    checkout_attempt_id='checkoutAttemptId0',
    funding_source=FundingSource.CREDIT,
    recurring_detail_reference='recurringDetailReference4',
    sdk_data='sdkData6',
    stored_payment_method_id='storedPaymentMethodId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

