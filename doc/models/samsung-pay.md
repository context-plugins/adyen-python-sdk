
# Samsung Pay

*This model accepts additional fields of type Any.*

## Structure

`SamsungPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSource`](../../doc/models/funding-source.md) | Optional | - |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `samsung_pay_token` | `str` | Required | The payload you received from the Samsung Pay SDK response.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type50`](../../doc/models/type-50.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.funding_source import FundingSource
from adyen.models.samsung_pay import SamsungPay

samsung_pay = SamsungPay(
    samsung_pay_token='samsungPayToken4',
    checkout_attempt_id='checkoutAttemptId2',
    funding_source=FundingSource.CREDIT,
    recurring_detail_reference='recurringDetailReference6',
    sdk_data='sdkData4',
    stored_payment_method_id='storedPaymentMethodId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

