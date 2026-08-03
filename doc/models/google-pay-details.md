
# Google Pay Details

*This model accepts additional fields of type Any.*

## Structure

`GooglePayDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSource`](../../doc/models/funding-source.md) | Optional | - |
| `google_pay_card_network` | `str` | Optional | The selected payment card network. |
| `google_pay_token` | `str` | Required | The `token` that you obtained from the [Google Pay API](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) `PaymentData` response.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `three_ds_2_sdk_version` | `str` | Optional | Required for mobile integrations. Version of the 3D Secure 2 mobile SDK.<br><br>**Constraints**: *Maximum Length*: `12` |
| `mtype` | [`Type24`](../../doc/models/type-24.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.funding_source import FundingSource
from adyen.models.google_pay_details import GooglePayDetails

google_pay_details = GooglePayDetails(
    google_pay_token='googlePayToken2',
    checkout_attempt_id='checkoutAttemptId6',
    funding_source=FundingSource.PREPAID,
    google_pay_card_network='googlePayCardNetwork6',
    recurring_detail_reference='recurringDetailReference0',
    sdk_data='sdkData0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

