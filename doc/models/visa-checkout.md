
# Visa Checkout

*This model accepts additional fields of type Any.*

## Structure

`VisaCheckout`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSource`](../../doc/models/funding-source.md) | Optional | - |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type55`](../../doc/models/type-55.md) | Optional | - |
| `visa_checkout_call_id` | `str` | Required | The Visa Click to Pay Call ID value. When your shopper selects a payment and/or a shipping address from Visa Click to Pay, you will receive a Visa Click to Pay Call ID. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.funding_source import FundingSource
from adyen.models.type_55 import Type55
from adyen.models.visa_checkout import VisaCheckout

visa_checkout = VisaCheckout(
    visa_checkout_call_id='visaCheckoutCallId4',
    checkout_attempt_id='checkoutAttemptId2',
    funding_source=FundingSource.DEBIT,
    sdk_data='sdkData4',
    mtype=Type55.VISACHECKOUT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

