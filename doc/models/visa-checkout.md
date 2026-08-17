
# Visa Checkout

## Structure

`VisaCheckout`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSourceEnum`](../../doc/models/funding-source-enum.md) | Optional | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type55Enum`](../../doc/models/type-55-enum.md) | Optional | **visacheckout**<br><br>**Default**: `"visacheckout"` |
| `visa_checkout_call_id` | `str` | Required | The Visa Click to Pay Call ID value. When your shopper selects a payment and/or a shipping address from Visa Click to Pay, you will receive a Visa Click to Pay Call ID. |

## Example

```python
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.type_55_enum import Type55Enum
from adyen.models.visa_checkout import VisaCheckout

visa_checkout = VisaCheckout(
    visa_checkout_call_id='visaCheckoutCallId4',
    checkout_attempt_id='checkoutAttemptId2',
    funding_source=FundingSourceEnum.DEBIT,
    sdk_data='sdkData4',
    mtype=Type55Enum.VISACHECKOUT
)
```

