
# Samsung Pay

## Structure

`SamsungPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSourceEnum`](../../doc/models/funding-source-enum.md) | Optional | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `samsung_pay_token` | `str` | Required | The payload you received from the Samsung Pay SDK response.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type50Enum`](../../doc/models/type-50-enum.md) | Optional | **samsungpay**<br><br>**Default**: `"samsungpay"` |

## Example

```python
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.samsung_pay import SamsungPay
from adyen.models.type_50_enum import Type50Enum

samsung_pay = SamsungPay(
    samsung_pay_token='samsungPayToken4',
    checkout_attempt_id='checkoutAttemptId2',
    funding_source=FundingSourceEnum.CREDIT,
    recurring_detail_reference='recurringDetailReference6',
    sdk_data='sdkData4',
    stored_payment_method_id='storedPaymentMethodId0',
    mtype=Type50Enum.SAMSUNGPAY
)
```

